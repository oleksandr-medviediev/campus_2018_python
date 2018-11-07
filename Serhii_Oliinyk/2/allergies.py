def allergies(digit):
    """Function searh all allergic items.

    Args:
        digit: type integer.

    Returns:
        Return the list of allergic items.

    """

    data = {
        "eggs": 1,
        "peanuts": 2,
        "shellfish": 4,
        "strawberries": 8,
        "tomatoes": 16,
        "chocolate": 32,
        "pollen": 64,
        "cats": 128
    }

    values = list(filter(lambda x: x <= digit, data.values()))
    values.reverse()

    digits = []

    for i in values:
        value = digit - i
        if(value >= 0):
            digits.append(i)
            digit = value

    result = []

    for k, v in data.items():
        if v in digits:
            result.append(k)

    return result


if __name__ == '__main__':
    result = allergies(34)
    print(result)
