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


print(checkTime(input('Time (or not time): ')))
