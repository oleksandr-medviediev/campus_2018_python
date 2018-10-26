import sys


def Castable(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

time = input("Enter time \n")

if len(time) != 5 or time[2] != ":":
    print(False)
    sys.exit()

hours = time[:2]
if Castable(hours) == False:
    print("not a valid time")
    sys.exit()
else:
    hours = int(hours)

am = True

if hours > 24 or hours < 0:
    print("not a valid time")
    sys.exit()
elif hours > 11:
    hours -= 12
    am = False

minutes = time[3:]
if Castable(minutes) == False:
    print("not a valid time")
    sys.exit()
else:
    minutes = int(minutes)

if minutes > 60 or minutes < 0:
    print("not a valid time")
    sys.exit()

if am == True:
    print(str(hours) + ":" + str(minutes) + " am")
else:
    print(str(hours) + ":" + str(minutes) + " pm")
