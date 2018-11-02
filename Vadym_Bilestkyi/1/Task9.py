from Task8 import is_valid_time


def from_24_to_12(time):
    if not is_valid_time(time):
        return 'Invalid time'

    hours, minutes = (int(time_part) for time_part in time.split(':'))
    day_part = 'am'

    if hours > 12:
        hours -= 12
        day_part = 'pm'

    return '{}:{} {}'.format(hours, minutes, day_part)


print(from_24_to_12('20:59'))
print(from_24_to_12('2:59'))
