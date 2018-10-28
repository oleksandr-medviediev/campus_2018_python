ZERO_TO_NINETEEN = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
                    'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen'
                    'eighteen', 'nineteen')

TENS = ('twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')

DENOMINATORS = {100: 'hundred', 1000: 'thousand', 1000000: 'million', 1000000000: 'billion', 1000000000000: 'trillion'}
DENOMINATOR_KEYS = tuple(DENOMINATORS.keys())


def spell_short_number(number):
    """
    Spells a number thad does not require a denominator.

    :param number: number in question.
    :type number: int.

    :return: the number spelt in English.
    :rtype: str.
    """
    if number < 20:
        result = ZERO_TO_NINETEEN[number]
    else:
        number_tens = TENS[number // 10 - 2]

        if number % 10:
            result = f'{number_tens}-{spell_number(number % 10)}'
        else:
            result = number_tens

    return result


def spell_long_number(number, denominator_value):
    """
    Spells a number that requires at least one denominator.

    :param number: number in question.
    :type number: int.

    :param denominator_value: biggest possible denominator for number.
    :type denominator_value: int.

    :return: the number spelt in English.
    :rtype: str.
    """
    denominator = DENOMINATORS[denominator_value]

    if number >= 2 * denominator_value:
        denominator = ''.join([denominator, 's'])

    result = f'{spell_number(number // denominator_value)} {denominator} {spell_number(number % denominator_value)}'
    return result


def determine_denominator_value(number):
    """
    Returns the biggest denominator value possible for number.

    :param number: the number in question.
    :type number: int.

    :return: the biggest denominator value possible for number.
    :rtype: int.
    """
    enumerator_value = 0

    for i, value in enumerate(DENOMINATOR_KEYS):

        if number < value:
            enumerator_value = DENOMINATOR_KEYS[i - 1]
            break

    return enumerator_value


def spell_number(number):
    """
    Returns the number spelt in English.

    :param number: number to spell
    :type number: int in range [0; 999999999999].

    :return: the number spelt in English.
    :rtype: str.
    """
    if number < 100:
        result = spell_short_number(number)
    else:
        result = spell_long_number(number, determine_denominator_value(number))

    return result
