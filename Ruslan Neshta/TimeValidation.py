def is_time_valid(string):
    numbers = string.split(':')
    is_valid = False

    if len(numbers) == 2 and numbers[0].isdigit() and numbers[1].isdigit():
        hours = int(numbers[0])
        minutes = int(numbers[1])

        if 0 <= hours <= 24 and 0 <= minutes <= 59:
            is_valid = True

    return is_valid


if __name__ == "__main__":
    time = input("Enter a time in 24 hour format: ")
    result = is_time_valid(time)
    print(result)
