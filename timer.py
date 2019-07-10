def definision_of_time(message):

    start_time = []

    for char in message:
        if char.isdigit():
            start_time.append(char)

    hour = start_time[0]+start_time[1]
    minute = start_time[2]+start_time[3]

