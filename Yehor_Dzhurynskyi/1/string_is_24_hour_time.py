def string_is_24_hour_time(string):
    digits = string.split(':')
    if len(digits) != 2:
        return False

    hours = digits[0]
    minutes = digits[1]

    if len(hours) != 2 or len(minutes) != 2:
        return False

    if not (hours.isdigit() and minutes.isdigit()):
        return False

    hours = int(hours)
    minutes = int(minutes)

    time_is_valid = hours >= 0 and hours <= 23 and minutes >= 0 and minutes <= 59

    return time_is_valid
