from openpyxl import load_workbook
import config


# разбор сообщения работника
def message_decoding(message):

    # определяем отправителя, убираем matrix...
    worker = message['sender'].split(':')[0]

    # считываем время, которое прислал работник
    time_1 = []
    for char in message['content']['body']:
        if char.isdigit():
            time_1.append(char)
    if len(time_1) < 4:
        time_1.insert(0, '0')
    time_1[0] = int(str(time_1[0]) + str(time_1[1]))
    time_1[1] = int(str(time_1[2]) + str(time_1[3]))
    time_1.pop(3)
    time_1.pop(2)

    return worker, time_1


# проверка отправленного времени. если отправленное отличается от реального на 15 минут, пишет Гасюку
def check_time(time_1, time_2):
    check_time = 0
    wrire_time = True
    print(time_1)
    print(time_2)
    check_hour = 60 * abs((int(time_1[0]) - int(time_2[0])))
    check_minute = abs(int(time_1[1]) - int(time_2[1]))
    if (check_hour - check_minute) > 15:
        wrire_time = False
    return wrire_time


# функция, которая выбирает нужную строку по совпадению даты
def what_cell(date, worker):
    import os

    year = str(date.year)

    month = date.month
    if len(str(month)) < 2:
        month = '0' + str(month)

    day = date.day
    if len(str(day)) < 2:
        day = '0' + str(day)

    cell_value_must_be = str(year) + '-' + str(month) + '-' + str(day)

    book_name = 'Y:/ГРАФИКИ/' + config.worker_list[worker] + '.xlsx'

    book = load_workbook(book_name)
    sheet = book.active
    found_string = False
    found_colomn = ''
    i = 1
    while found_string == False:
        if cell_value_must_be in str(sheet[i][0].value):
            found_string = True
            a = str(sheet[i][1].value)
            if str(sheet[i][1].value) == 'None':
                found_colomn = 'B'
            else:
                found_colomn = 'G'
        else:
            i += 1

    return book_name, str(found_colomn + str(i))
