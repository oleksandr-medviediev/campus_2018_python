def checkTime(timeString):
    hoursAndMinutes = timeString.split(':')

    if len(hoursAndMinutes) != 2:
        return False

    if not (hoursAndMinutes[0].isdigit() and hoursAndMinutes[1].isdigit()):
        return False

    hours, minutes = int(hoursAndMinutes[0]), int(hoursAndMinutes[1])

    if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
        return False

    return True


def Convert24HourTimeTo12HourTime(timeString):
    if not checkTime(timeString):
        return "not a valid time"

    hoursAndMinutes = timeString.split(':')
    hours = int(hoursAndMinutes[0])

    minutesString = hoursAndMinutes[1]

    if hours <= 12:
        return timeString + ' am'
    else:
        return timeString.replace(str(hours), str(hours - 12)) + ' pm'

print(Convert24HourTimeTo12HourTime(input('Time: ')))
