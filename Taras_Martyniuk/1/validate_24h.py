
def main():
    time_str = input()
    print(is_valid_24h(time_str))


def is_valid_24h(time_str):
    if len(time_str) != 5:
        return False

    hours_str = time_str[:2]
    minutes_str = time_str[3:]

    if not hours_str.isdigit() and not minutes_str.isdigit():
        return False

    hours, minutes =  int(hours_str), int(minutes_str)

    return hours >= 0 and hours <= 23 and \
        minutes >= 0 and minutes <= 59

if __name__ == "__main__":
    main()