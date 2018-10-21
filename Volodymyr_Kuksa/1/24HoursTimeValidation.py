input_string = input('input 24 hour time that needs validation (format: hh:mm): ')

if len(input_string) != 5\
        or input_string[2] != ':'\
        or not input_string[:2].isdigit()\
        or not input_string[3:].isdigit():
    print(False)
    exit()

split_time = input_string.split(':')

hours = int(split_time[0])
minutes = int(split_time[1])

if hours < 0 or hours > 23:
    print(False)
elif minutes < 0 or minutes > 59:
    print(False)
else:
    print(True)

