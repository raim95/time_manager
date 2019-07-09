from matrix_client.client import MatrixClient
from matrix_client.room import Room
#from matrix_client.api import MatrixHttpApi
import config

work_client = MatrixClient(config.url)
work_client.login(config.login, config.password)
#rooms_ids = work_client.rooms
#work_api=MatrixHttpApi(config.url, work_client)

#rooms_ids_list = []

#for key in rooms_ids.keys():
#    room_id = str(key).split(":")[0]
#   rooms_ids_list.append(str(room_id))
#    room_name = str(work_client.rooms[key].name)
#    if room_name != "None":
#       print(str(rooms_ids_list.index(room_id)) + ' - ' + room_id + ' : ' + room_name)

#room_number = int(input('Please, choise room: '))
#current_room = Room(work_client, rooms_ids_list[room_number])
#print(current_room.display_name)

room_to_listen = Room( work_client, config.test_id)

def on_message(room, event):
    if event['type'] == 'm.room.message':
        print ("Hello!")
        print(room)
        print(event)

def main():
    room_to_listen.add_listener(on_message)
    work_client.start_listener_thread()
    work_client.listen_forever()

if __name__ == '__main__':
    main()


