def is_time_valid(time):
    if len(time) != 5 \
            or time[2] != ':' \
            or not time[:2].isdigit() \
            or not time[3:].isdigit():
        return False

    h = int(time[:2])
    m = int(time[3:])

    if h < 0 or h > 23:
        return False
    elif m < 0 or m > 59:
        return False

    return True


input_string = input('enter 24 hour time that needs to be converted to 12 hour format: ')

if not is_time_valid(input_string):
    print('not a valid time')
    exit()

split_time = input_string.split(':')

hours = int(split_time[0])
minutes = int(split_time[1])

is_am = hours < 12

if hours == 12 and minutes == 0:
    print('12:00 am')
elif hours == 0 and minutes == 0:
    print('12:00 pm')
elif is_am:
    print(input_string + ' am')
else:
    print(f'{hours - 12}:{minutes}')
