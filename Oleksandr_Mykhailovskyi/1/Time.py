import time

timeString = input("Enter time\n")

try:
# This will raise an exeption if smth's wrong
    t = time.strptime(timeString, '%H:%M')
except ValueError:
    print("Oups, non-valid format, try %H:%M (e.g. 12:13)")
else:
    print("Success")