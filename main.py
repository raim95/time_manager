from matrix_client.client import MatrixClient
from matrix_client.room import Room
# from matrix_client.api import MatrixHttpApi
import config


def main():
    work_client = MatrixClient(config.url)
    work_client.login(config.login, config.password)

    room_to_listen = Room(work_client, config.test_id)

    def on_message(room, event):
        if event['type'] == "m.room.message":
            room_to_listen.send_text("Hello!")
            #print(room)
           # print(event)

    room_to_listen.add_listener(on_message)
    work_client.start_listener_thread()
    work_client.listen_forever()

if __name__ == '__main__':
    main()
