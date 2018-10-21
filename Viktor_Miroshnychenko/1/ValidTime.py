import sys
time = input("Print  time \n")

def Castable(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if len(time) != 5 or time[2] != ":":
    print(False)
    sys.exit()

hours = time[0:2]
if Castable(hours) == False:
    print(False)
    sys.exit()
else:
    hours = int(hours)

minutes = time[3:]
if Castable(minutes) == False:
    print(False)
    sys.exit()
else:
    minutes = int(minutes)

if hours > 24 or minutes > 60 or hours < 0 or minutes < 0:
    print(False)
    sys.exit()

print(True)
