
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

input_time = input("enter time to validate")

print(is_valid_time(str(input_time)))
