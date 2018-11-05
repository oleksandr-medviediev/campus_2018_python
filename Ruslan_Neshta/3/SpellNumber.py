def spell_number_of(number, bound, word):
    """
    Spell out number in English

    :param number:  An integer number
    :param bound: An integer number that bounds check
    :param word: Text representation of bound
    :return: Text representation of billions in number
    :rtype: list
    """

    counts = number // bound
    rest = number % bound

    if counts > 1:
        word += 's'

    result = spell_number(counts)
    result.extend([word])

    if rest != 0:
        result.extend(spell_number(rest))

    return result


def spell_billions(number):
    """
    Spell out number of billions in English

    :param number:  A number from 0 to 999 999 999 999.
    :return: Text representation of billions in number
    :rtype: list
    """

    result = spell_number_of(number, 1000000000, 'billion')
    return result


def spell_millions(number):
    """
    Spell out number of millions in English

    :param number:  A number from 0 to 999 999 999.
    :return: Text representation of millions in number
    :rtype: list
    """

    result = spell_number_of(number, 1000000, 'million')
    return result


def spell_thousands(number):
    """
    Spell out number of thousands in English

    :param number:  A number from 0 to 999 999.
    :return: Text representation of thousands in number
    :rtype: list
    """

    result = spell_number_of(number, 1000, 'thousand')
    return result


def spell_hundreds(number):
    """
    Spell out number of hundreds in English

    :param number:  A number from 0 to 999.
    :return: Text representation of hundreds in number
    :rtype: list
    """

    result = spell_number_of(number, 100, 'hundred')
    return result


def spell_to_hundred(number):
    """
    Spell out number in English

    :param number:  A number from 0 to 99.
    :return: Text representation of a number
    :rtype: list
    """

    digits = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }

    numbers_11_19 = {
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen'
    }

    tens_10_100 = {
        10: 'ten',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety'
    }

    result = []

    ones = number % 10
    tens = number / 10

    tens_container = numbers_11_19
    if number < 10:
        tens = 0

    elif number >= 20:
        tens_container = tens_10_100
    else:
        ones = 0

    if tens > 0:
        tens = int(tens * 10)

        if tens > 20:
            tens = number // 10 * 10

        result.append(tens_container[tens])

    if ones != 0 and len(result) != 0:
        if tens > 10:
            result[-1] = result[-1] + '-' + digits[ones]

    elif number == 0:
        result.append(digits[number])

    elif ones != 0:
        result.append(digits[ones])

    return result


def spell_number(number):
    """
    Spell out number in English.

    :param number: A number from 0 to 999 999 999 999.
    :return: Text representation of a number
    :rtype: list
    """

    result = []
    if number >= 1000000000:
        result.extend(spell_billions(number))

    elif number >= 1000000:
        result.extend(spell_millions(number))

    elif number >= 1000:
        result.extend(spell_thousands(number))

    elif number >= 100:
        result.extend(spell_hundreds(number))

    else:
        result.extend(spell_to_hundred(number))

    return result


def say_number(number):
    """
    Spell out number in English.

    :param number: A number from 0 to 999 999 999 999.
    :return: Text representation of a number
    :rtype: str
    """

    spellings = spell_number(number)
    text = " ".join(spellings)
    return text


if __name__ == "__main__":
    res = say_number(14)
    print("14:", res)

    res = say_number(100)
    print("100:", res)

    res = say_number(120)
    print("120:", res)

    res = say_number(1002)
    print("1002:", res)

    res = say_number(1323)
    print("1323:", res)

    res = say_number(13235768432)
    print("13 235 768 432:", res)
