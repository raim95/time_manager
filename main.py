from typing import Any, Union
from matrix_client.client import MatrixClient
import time
import config
from defs import *
from datetime import datetime
import openpyxl
from openpyxl import load_workbook
import os

work_client = MatrixClient(config.url)  # инициализуруем клиента

work_client.login(config.login, config.password)  # логинимся

room_to_listen = work_client.join_room(config.room_id)  # инициируем комнату

def on_message(room, event):
    if event['type'] == "m.room.message":
        #if event['sender'] != "@RuslanRamazanov:matrix.restautomat.ru" \
        #        and event['sender'] != "@Jasur:matrix.restautomat.ru" \
        #       and event['sender'] != "@ATagibov:matrix.restautomat.ru":

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
        #write_time = check_time(time_1, time_2)
        #if write_time == False:
        #    agasuk_room = work_client.join_room(config.test_id) # комната Гасюка
        #    agasuk_room.send_text(config.worker_list[worker]+' указал неверное время')

        # вычисляем графу, в которую надо записать время
        book_to_write, cell_for_write = what_cell(sending_time, worker)

        # записываем время в ячейку
        book = load_workbook(book_to_write)
        sheet = book.active
        sheet[cell_for_write] = str(time_2[0])+':'+str(time_2[1])+"("+str(time_1[0])+":"+str(time_1[1]+")")
        try:
            book.save(book_to_write)
        except PermissionError:
            agasuk_room = work_client.join_room(config.agasuk) # инициируем комнату с Гасюком
            agasuk_room.send_text('Не могу сохранить документ "'+book_to_write+ '"')

room_to_listen.add_listener(on_message)  # добавляем слушателя
work_client.start_listener_thread()  # запускаем тред слушателя
alexey_room = work_client.join_room(config.test_id)
alexey_room.send_text('Bot started.')

while True:
    pass