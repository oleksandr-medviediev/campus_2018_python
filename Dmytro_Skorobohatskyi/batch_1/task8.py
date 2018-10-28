string = input('enter the string\n')

is_time_valid = True

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

print(is_time_valid)
