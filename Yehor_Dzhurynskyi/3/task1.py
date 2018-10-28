NUM_TO_TEXT = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'fourty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninety'
}

NUM_POS_TO_TEXT = {
    0: 'hundred',
    1: 'thousand'
}


def number_to_text(num):

    text_list = []
    num_str = str(num)
    if num_str in NUM_TO_TEXT:
        return NUM_TO_TEXT[num_str]

    suffix = num_str[-2:].lstrip('0')

    if suffix in NUM_TO_TEXT:
        text_list.append(NUM_TO_TEXT[suffix])
    elif len(suffix) == 2:

        decades = NUM_TO_TEXT[suffix[0] + '0']
        ones = NUM_TO_TEXT[suffix[1]]
        text_list.append(f'{decades}-{ones}')

    prefix = num_str[:-2]
    if len(prefix) > 0 and len(suffix) > 0:
        text_list.append('and')

    for position, digit in enumerate(reversed(prefix)):

        if digit == '0':
            continue

        if position in NUM_POS_TO_TEXT:
            text_list.append(NUM_POS_TO_TEXT[position])

        text_list.append(NUM_TO_TEXT[digit])
    text = ' '.join(reversed(text_list))

    return text


def say_number(num):
    print(f'{str(num)}={number_to_text(num)}')
