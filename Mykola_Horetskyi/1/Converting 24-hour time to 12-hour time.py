def is24HourTime(time):
    if len(time) != 5:
        return False
    elif not time[:2].isdigit() or not time[3:].isdigit() or time[2] != ':':
        return False
    elif int(time[:2]) < 0 or int(time[:2]) > 24 or int(time[3:]) < 0 or int(time[3:]) > 59:
        return False
    return True

input_time = input('input time:\n')

if is24HourTime(input_time):
    hours = int(input_time[:2])
    if hours >= 12 and hours < 20:
        converted_time ='0' + str(hours - 12) + input_time[2:] + ' pm'
    elif hours >= 22:
        converted_time = str(hours - 12) + input_time[2:] + ' pm'
    else:
        converted_time = input_time + ' am'
        
    print(converted_time)

else:
    print('not a valid time')
