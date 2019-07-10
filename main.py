from matrix_client.client import MatrixClient
import time
import config
import timer

work_client = MatrixClient(config.url)  # инициализуруем клиента

work_client.login(config.login, config.password)  # логинимся

room_to_listen = work_client.join_room(config.test_id)  # инициируем комнату


def on_message(room, event):
    if event['type'] == "m.room.message":
        #room_to_listen.send_text("Im work! Message!")
        definition_of_time(event['content']['body'])
    else:
        print(event['type'])

room_to_listen.add_listener(on_message) # добавляем слушателя
work_client.start_listener_thread()  # запускаем тред слушателя

while True:
    pass
