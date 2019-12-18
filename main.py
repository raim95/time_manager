from matrix_client.client import MatrixClient
from defs import *
from datetime import datetime
from openpyxl import load_workbook
import time
import getpass

#для тестов. На ПК Гасюка записать пароль в файле config
password = getpass.getpass()

work_client = MatrixClient(config.url)  # инициализуруем клиента

work_client.login(config.login, password)  # логинимся

room_to_listen = work_client.join_room(config.room_id)  # инициализируем комнату
alexey_room = work_client.join_room(config.apoluyanov)
agasuk_room = work_client.join_room(config.agasuk)

# функция, которую вызывает листенер
def on_message(room, event):
    if event['type'] == "m.room.message" \
    and event['content']['body'] != 'Bot started.'\
    and 'Service messange:' not in event['content']['body']:
        # приводим системное время к человекочитаемому виду
        sending_time = datetime.now()
        time_2 = [0, 0]
        if len(str(sending_time.hour)) < 2:
            time_2[0] = '0' + str(sending_time.hour)
        else:
            time_2[0] = sending_time.hour

        if len(str(sending_time.minute)) < 2:
            time_2[1] = '0' + str(sending_time.minute)
        else:
            time_2[1] = sending_time.minute

        # получаем сотрудника и время, которое он прислал
        worker, time_1, date, found_colomn, missundestand = message_decoding(event)

        if missundestand == True:
            alexey_room.send_text('missundestand = True')
            alexey_room.send_text(worker)
            alexey_room.send_text(event['content']['body'])

        elif date != '':
            alexey_room.send_text(str(worker) + ' ' + 'date = ' + str(date))

        elif found_colomn != '':
            alexey_room.send_text(str(worker) + ' ' + str(event['content']['body']) + ' ' + str(found_colomn))

        elif len(time_1) > 2:
            alexey_room.send_text(str(worker) + ' ' + 'Time = ' + str(time_1))

        # если мы получили сообщение в том виде, в котором ожидали
        else:
            # проверяем соответвие написанного и реального времени
            write_time = check_time(time_1, time_2)

            if write_time == True:
                time_3 = str(time_2[0]) + ':' + str(time_2[1])
            else:
                time_3 = str(time_2[0]) + ':' + str(time_2[1]) + "(" + str(time_1[0]) + ":" + str(time_1[1]) + ")"

            # вычисляем ячейку, в которую надо записать время
            book_to_write, cell_for_write = what_cell(sending_time, worker)

            # записываем время в ячейку
            book_saved = False
            book = load_workbook(book_to_write)
            sheet = book.active
            sheet[cell_for_write] = time_3
            while book_saved == False:
                try:
                    book.save(book_to_write)
                    book_saved = True
                except:
                    agasuk_room.send_text('Не могу сохранить документ "' + book_to_write + '"')
                    book_saved = False
                    time.sleep(30)



room_to_listen.add_listener(on_message)  # добавляем слушателя
#alexey_room.add_listener(on_message) # тестовая комната с саппортом
work_client.start_listener_thread()  # запускаем тред слушателя

alexey_room.send_text('Bot started.')
#agasuk_room.send_text('Bot started.')

while True:
    time.sleep(1)
