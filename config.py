url = 'https://matrix.restautomat.ru:18448'
login = "Support"
password = "hi4r8wdjkghds"
room_id = "!JtYomtSYacVfwKHWig:matrix.restautomat.ru" # Рабочий графие
test_id = "!LXrUwoulMygVTSestO:matrix.restautomat.ru" # Полуянов А
agasuk = '!mJOcrcJtbgGjfWOtmR:matrix.restautomat.ru' # Гасюк А
worker_list = \
    {
        '@APoluyanov':'Полуянов А.',
        '@AGasyuk' : 'Гасюк А.',
        "@CTO" : "Софийский С.",
        "@VRogach" : "Рогач В.",
        "@Gosip" : "Осипян Г.",
        "@RRamazanov" : "Рамазанов Риман.",
        "@lutfullin" : "Лутфуллин Т.",
        "@Sklad1" : "Сапрыкин Д.",
        "@nrahmanyuk" : "Рахманюк Н.",
        "@aprozorovskii" : "Прозоровский А.",
        "@EPushkarkiy" : "Пушкарский Е.",
        "@RuslanRamazanov" : 'Рамазанов Руслан',
        "@Jasur" : "Каримов Ж.",
        "@ATagibov" : "Тагибов А."
    }

# worker - id сотрудника, приславшего соощение
# book - книга экселя, в которой ведётся учёт
# time_1 - время, которое прислал сотрудник
# time_2 - время отправки сообщения
# check_time - флаг соответствия написанного и реального времени
# cell_for_write - ячейка таблицы, в которую надо записать время
# cell_value_must_be - значение ячейки, которое мы ищем в таблице
# found_string - флаг поиска нужной строки
# book_to_write - файл, в котором ведётся учёт времени сотрулника
# worker_list - словарь соответствия айдишников и фамилий сотрудников
# time_write - флаг, который поднимается в том случае, если разница между отправленным и системным временем больше 15 мин

# def on_message(room, event): функция, которая запускается, когда приходит сообщение
#
# def message_decoding(message, sending_time): функция разбора сообщения. На вход получает объект "event"
# Возвращает имя/фамилию сотрудника (worker) и время, которое он указал в человеческом формате чч:мм (time_1)
# def check_time(time_1, time_2): проверяет отправленное и реальное время. Если разница больше 15 минут, пишет Гасюку
#
#
#