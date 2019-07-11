# разбор сообщения работника
def message_decoding(message, sending_time):

    # определяем отправителя, убираем matrix...
    worker = message['sender'].split(':')[0]

    # считываем время, которое прислал работник
    wried_time = []
    for char in message['content']['body']:
        if char.isdigit():
            wried_time.append(char)

    hour = wried_time[0]+wried_time[1]
    minute = wried_time[2]+wried_time[3]
    worker_writed_time = hour + ':' + minute

    # форматируем время отправки
    real_time = str(sending_time.hour) + ':' + str(sending_time.minute)

    return worker, worker_writed_time, real_time