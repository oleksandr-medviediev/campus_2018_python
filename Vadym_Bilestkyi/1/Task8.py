def is_valid_time(time):
    try:
        hours, minutes = time.split(':')
    except ValueError:
        return False

    return 0 <= int(hours) < 24 and 0 <= int(minutes) < 60


if __name__ == '__main__':
    print(is_valid_time('13:58'))
    print(is_valid_time('28:74'))
    print(is_valid_time('18'))
    print(is_valid_time('1544'))