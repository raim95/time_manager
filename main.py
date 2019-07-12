from matrix_client.client import MatrixClient
import time
import config
from defs import *
from datetime import datetime
import openpyxl
from openpyxl import load_workbook

work_client = MatrixClient(config.url)  # инициализуруем клиента

work_client.login(config.login, config.password)  # логинимся

room_to_listen = work_client.join_room(config.test_id)  # инициируем комнату


def on_message(room, event):
    if event['type'] == "m.room.message":

        # приводим системное время к человекочитаемому виду
        sending_time = datetime.now()
        time_2 = [0, 0]
        time_2[0] = str(sending_time.hour)
        if len(str(sending_time.minute)) < 2:
            time_2[1] = '0' + str(sending_time.minute)
        else:
            time_2[1] = sending_time.minute

        # получаем сотрудника и время, которое он прислал
        worker, time_1 = message_decoding(event)

        # проверяем соответвие написанного и реального времени
        check_time(time_1, time_2)

        # вычисляем графу, в которую надо записать время
        cell_for_write = what_cell(sending_time, worker)

        # записываем время в ячейку
        book = load_workbook(worker+'.xlsx')
        sheet = book.active
        sheet[cell_for_write] = str(time_2[0])+':'+str(time_2[1])+"("+str(time_1[0])+":"+str(time_1[1]+")")
        book.save(worker+'.xlsx')


room_to_listen.add_listener(on_message)  # добавляем слушателя
work_client.start_listener_thread()  # запускаем тред слушателя

while True:
    pass
