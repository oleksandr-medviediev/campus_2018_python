time = input('input time:\n')

isValid = True

if len(time) != 5:
    isValid = False
elif not time[:2].isdigit() or not time[3:].isdigit():
    isValid = False
elif int(time[:2]) < 0 or int(time[:2]) > 24 or int(time[3:]) < 0 or int(time[3:]) > 59:
    isValid = False

print(isValid)
