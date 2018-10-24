
def is_valid_time(input_time):
    if len(input_time) != 5:
        return False
    elif input_time[2] != ':':
        return False
    elif int(input_time[:2]) > 23:
        return False
    elif int(input_time[3:5]) > 59:
        return False
    else:
        return True

input_time = input("enter time to convert: ")

if is_valid_time(str(input_time)):
    day_part = ""

    if int(input_time[:2]) > 12:
        day_part = " pm"
        hours = int(input_time[:2]) % 12
        hours = str(hours)

    else:
        day_part = " am"
        hours = input_time[:2]

    print(hours + input_time[2:5] + day_part)

else:
    print("not a valid time")
