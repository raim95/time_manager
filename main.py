from matrix_client.client import MatrixClient
from defs import *
from datetime import datetime
from openpyxl import load_workbook

work_client = MatrixClient(config.url)  # инициализуруем клиента

work_client.login(config.login, config.password)  # логинимся

room_to_listen = work_client.join_room(config.test_id)  # инициируем комнату


# функция, которую вызывает листенер
def on_message(room, event):
    if event['type'] == "m.room.message" and event['content']['body']!='Bot started.':
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
        worker, time_1, date, found_colomn = message_decoding(event)

        if date != '':
            pass

        elif found_colomn != '':
            pass

        elif len(time_1) > 2:
            pass
        # проверяем соответвие написанного и реального времени
        else:
            write_time = check_time(time_1, time_2)

            # если реальное время отличается от времени, написанного сотрудником, сообщаем об этом
            if write_time == True:
                time_3 = str(time_2[0]) + ':' + str(time_2[1])
            else:
                time_3 = str(time_2[0]) + ':' + str(time_2[1]) + "(" + str(time_1[0]) + ":" + str(time_1[1]) + ")"

            # вычисляем ячейку, в которую надо записать время
            book_to_write, cell_for_write = what_cell(sending_time, worker)

            # записываем время в ячейку
            book = load_workbook(book_to_write)
            sheet = book.active
            sheet[cell_for_write] = time_3
            try:
                book.save(book_to_write)
            except PermissionError:
                agasuk_room = work_client.join_room(config.agasuk)  # инициируем комнату с Гасюком
                agasuk_room.send_text('Не могу сохранить документ "' + book_to_write + '"')


room_to_listen.add_listener(on_message)  # добавляем слушателя
work_client.start_listener_thread()  # запускаем тред слушателя

#alexey_room = work_client.join_room(config.test_id)
#alexey_room.send_text('Bot started.')

room_to_listen.send_text('Bot started.')

while True:
    pass