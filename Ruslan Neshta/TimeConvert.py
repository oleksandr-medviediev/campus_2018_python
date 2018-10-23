import TimeValidation


def convert_24h_to_12h_time(string):
    formatted_time = "not a valid time"

    if TimeValidation.is_time_valid(string):
        numbers = string.split(':')
        hours = int(numbers[0])

        if hours > 12:
            formatted_time = str.join("", [str(hours - 12), ':', numbers[1], ' pm'])
        else:
            formatted_time = str.join("", [numbers[0], ':', numbers[1], ' am'])

    return formatted_time


if __name__ == "__main__":
    time = input("Enter a time in 24 hour format: ")
    result = convert_24h_to_12h_time(time)
    print(result)
