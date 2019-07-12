from openpyxl import load_workbook

# разбор сообщения работника
def message_decoding(message):
    # определяем отправителя, убираем matrix...
    worker = message['sender'].split(':')[0]

    # считываем время, которое прислал работник
    time_1 = []
    for char in message['content']['body']:
        if char.isdigit():
            time_1.append(char)

    time_1[0] = str(time_1[0] + str(time_1[1]))
    time_1[1] = str(time_1[2]) + str(time_1[3])

    return worker, time_1


# проверка отправленного времени. если отправленное отличается от реального на 15 минут, пишет Гасюку

def check_time(time_1, time_2):
    check_time = 0
    if abs((int(time_1[0]) - int(time_2[0]) == 0)):
        check_time += 1
    if abs((int(time_1[1]) - int(time_2[1]) == 0)):
        check_time += 1
    if check_time != 2:
        print('Wrong time')
#        from matrix_client.room import Room
#        agasroom = Room(work_client, config.agasuk)

# функция, которая выбирает нужную строку по совпадению даты
def what_cell(date, worker):

    year = str(date.year)

    month = date.month
    if len(str(month)) < 2:
        month = '0' + str(month)

    day = date.day
    if len(str(day)) < 2:
        day = '0' + str(day)

    cell_value_must_be = str(year)+'-'+str(month)+'-'+str(day)

    book = load_workbook(worker+'.xlsx')
    sheet = book.active
    found_string = False
    i = 1
    while found_string == False:
        if cell_value_must_be in str(sheet[i][0].value):
            found_string = True
        else: i+=1

    return str('B'+str(i))