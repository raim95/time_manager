from openpyxl import load_workbook
import config


# если время не указано
def no_time_im_message(message, missundestand):
    found_colomn = ''
    message = message.split(' ')

    for word in message:
        if word in config.status_start:
            found_colomn = 'B'
        elif word in config.status_finish:
            found_colomn = 'G'
        else: missundestand = True
    return found_colomn, missundestand


# если указано только время
def only_time_in_message(time_1):
    if len(time_1) == 3 or len(time_1) == 7:
        time_1.insert(0, '0')
    if len(time_1) == 4:
        time_1[0] = str(time_1[0]) + str(time_1[1])
        time_1[1] = str(time_1[2]) + str(time_1[3])
        time_1.pop(3)
        time_1.pop(2)
    elif len(time_1) == 8:
        time_1[0] = str(time_1[0]) + str(time_1[1])
        time_1[1] = str(time_1[2]) + str(time_1[3])
        time_1[2] = str(time_1[4]) + str(time_1[5])
        time_1[3] = str(time_1[6]) + str(time_1[7])
        for i in range(4):
            time_1.pop(4)
    return time_1


# если указано время и дата
def time_and_date_in_message(time_1):
    time_1_whis_date = {'date': '', 'time_1': ''}
    # получаем дату
    time_1_whis_date['date'] = \
        str(time_1[0]) + str(time_1[1]) + '.' \
        + str(time_1[2]) + str(time_1[3]) + '.' + "2019"
    # убираем дату из сообщения
    for i in range(4):
        time_1.pop(0)
    # записываем дату и время
    time_1_whis_date['time_1'] = only_time_in_message(time_1)
    found_colomn = time_1_whis_date['date']
    time_1 = time_1_whis_date['time_1']
    return found_colomn, time_1


# разбор сообщения работника
def message_decoding(message):
    missundestand = False

    # определяем отправителя, убираем matrix...
    worker = message['sender'].split(':')[0]

    # считываем время, которое прислал работник
    date = ''
    found_colomn = ''
    time_1 = []
    # ищем цифры в сообщении
    for char in message['content']['body']:
        if char.isdigit():
            time_1.append(char)
    # если цифр нет, проверяем сообщение на соответствие элементам из status
    if len(time_1) == 0:
        found_colomn, missundestand = no_time_im_message(str(message['content']['body']), missundestand)

    # если цифры есть, определяем их количество и запускаем нужную функцицию
    elif len(time_1) >= 3 and len(time_1) <= 8:
        time_1 = only_time_in_message(time_1)
    elif len(time_1) >= 11 and len(time_1) <= 12:
        date, time_1 = time_and_date_in_message(time_1)

    # если цифр больше чем надо
    else: missundestand = True

    return worker, time_1, date, found_colomn, missundestand


# проверка отправленного времени. если отправленное отличается от реального на 15 минут, пишет Гасюку
def check_time(time_1, time_2):
    wrire_time = True
    check_hour = 60 * abs((int(time_1[0]) - int(time_2[0])))
    check_minute = abs(int(time_1[1]) - int(time_2[1]))
    if (check_hour - check_minute) > 15:
        wrire_time = False
    return wrire_time


# функция, которая выбирает нужную строку по совпадению даты
def what_cell(date, worker):

    year = str(date.year)

    month = date.month
    if len(str(month)) < 2:
        month = '0' + str(month)

    day = date.day
    if len(str(day)) < 2:
        day = '0' + str(day)

    cell_value_must_be = str(year) + '-' + str(month) + '-' + str(day)

    book_name = config.way_to_files + config.worker_list[worker] + '.xlsx'

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
