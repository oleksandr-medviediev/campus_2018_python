input_string = input('Enter a string\n')

acceptable_char = [str(i) for i in range(10)]

time = input_string.split(":")

if len(time) != 2:
    print("not a valid time")
    quit()

for string in time:
    if len(string) != 2:
        print("not a valid time")
        quit()
    for ch in string:
        if ch not in acceptable_char:
            print("not a valid time")
            quit()

if int(time[0]) >= 24 or int(time[0]) < 0:
    print("not a valid time")
    quit()
elif int(time[0]) >= 12:
    time[0] = str(int(time[0]) - 12)
    time.append('pm')
else:
    time.append('am')

if len(time[0]) == 1:
    time[0] = "0" + time[0]

if int(time[1]) >= 60 or int(time[0]) < 0:
    print("not a valid time")
    quit()

output_string = time[0] + ':' + time[1] + ' ' + time[2]

print(output_string)
