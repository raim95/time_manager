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
        sending_time = datetime.now()
        worker, worker_time, real_time = message_decoding(event, sending_time)

        book = openpyxl.load_workbook('graphs.xlsx')
        book_list = book['Полуянов А.']
        book_list['B5'] = worker_time
        book_list['B6'] = real_time
        book.save('graphs.xlsx')
        print('exelent')

room_to_listen.add_listener(on_message) # добавляем слушателя
work_client.start_listener_thread()  # запускаем тред слушателя

while True:
    pass