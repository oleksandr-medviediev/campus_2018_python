string = input('enter the string\n')

is_time_valid = True

hours = minutes = 0

colon_index = string.find(":")
if colon_index == -1:
    is_time_valid = False
else:
    numbers = string.split(':')

    for i in range(len(numbers)):
        if numbers[i].isdigit() and len(numbers[i]) == 2:
            numbers[i] = int(numbers[i])
        else:
            is_time_valid = False

    if is_time_valid == True:
        hours = numbers[0]
        minutes = numbers[1]

        if hours >= 24 or minutes >= 60:
            is_time_valid = False


if is_time_valid:
    day_part = "am"
    if hours > 12:
        day_part = "pm"
        hours -= 12

    formatted_time = '{}:{} {}'.format(hours, minutes, day_part)
    print(formatted_time)
else:
    print("not a valid time")
