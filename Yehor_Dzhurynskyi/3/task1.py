NUM_TO_TEXT = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'fourty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}

TRIPLE_NUM_TO_TEXT = {
    1: 'thousand',
    2: 'million',
    3: 'billion'
}


def dozen_to_text(dozen):
    """
    converts dozen num-representation to text-representation
        :param num dozen: number that should be converted
        :return: lixical representation of dozen
        :rtype: str
    """

    if dozen in NUM_TO_TEXT:
        decade_text = NUM_TO_TEXT[dozen]
    else:

        decades = dozen // 10 * 10
        ones = dozen % 10
        decade_text = f'{NUM_TO_TEXT[decades]}-{NUM_TO_TEXT[ones]}'

    return decade_text


def number_to_text(num):
    """
        :param int num: integer number from 0 to 999999999999
        :return: textual representation of number
        :rtype: str
    """

    text_list = []
    if num in NUM_TO_TEXT:
        return NUM_TO_TEXT[num]

    num_of_triple = 0
    while (num > 0):

        if num_of_triple > 0:
            text_list.append(TRIPLE_NUM_TO_TEXT[num_of_triple])

        triple = num % 1000
        hundred = triple // 100
        dozen = triple % 100

        if dozen > 0:

            text_list.append(dozen_to_text(dozen))
            if num_of_triple == 0:
                text_list.append('and')

        if hundred > 0:

            text_list.append('hundred')
            text_list.append(NUM_TO_TEXT[hundred])

        num //= 1000
        num_of_triple += 1

    return ' '.join(reversed(text_list))


def say_number(num):
    """
    prints integer number in textual representation
        :param int num: number which sould be printed
    """

    print(f'{str(num)}={number_to_text(num)}')
