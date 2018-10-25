input_string = input('Enter a string\n')

acceptable_char = [str(i) for i in range(10)]

time = input_string.split(":")

if len(time) != 2:
    print(False)
    quit()

for string in time:
    if len(string) != 2:
        print(False)
        quit()
    for ch in string:
        if ch not in acceptable_char:
            print(False)
            quit()

if int(time[0]) >= 24 or int(time[0]) < 0:
    print(False)
    quit()

if int(time[1]) >= 60 or int(time[0]) < 0:
    print(False)
    quit()

print(True)
