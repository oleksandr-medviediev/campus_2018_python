def spell_number(number):
    """
    Function spell out number less than 1000000000 in English
    Args:
        number(int): number to spell
    Returns:
        str: string with spelled number
    """
    if number > 999999999999:
        return "wrong number!"

    num_string = unifying([ch for ch in str(number)])
    return_string = []
    exponents = ['thousand', 'million', 'billion']
    for i in range(0, 12, 3):
        if int(''.join(num_string[i:i + 3])) != 0:
            return_string.append(spell_number_less_then_thousand(''.join(num_string[i:i + 3]), i == 9))

    size_of_list = len(return_string)
    for i in range(len(return_string) - 1, 0, -1):
        return_string.insert(i, exponents[size_of_list - 1 - i])

    return ' '.join(return_string)


def unifying(number_str):

    if len(number_str) < 12:
        for i in range(12 - len(number_str)):
            number_str.insert(0, '0')
    return number_str


def spell_number_less_then_thousand(num_string, add_and):
    """
    Function spell out number less than 1000 in English
    Args:
        num_string(str): number to spell
        add_and(bool): if true there will be 'and'  between hundreds and tens
    Returns:
        str: string with spelled number
    """
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
               'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['zero', 'ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    spelling = []
    if int(num_string[0]) != 0:

        spelling.append(numbers[int(num_string[0])] + ' hundred')
        if int(num_string[1] + num_string[2]) != 0 and add_and:
            spelling.append("and")

    if int(num_string[1]) in [0, 1]:
        spelling.append(numbers[int(num_string[1] + num_string[2])])
    elif int(num_string[1]) > 1:
        spelling.append(tens[int(num_string[1])] + ' ' + numbers[int(num_string[2])])

    return ' '.join(spelling)


def spell_number_less_then_thousand_german(num_string):
    """
    Function spell out number less than 1000 in German
    Args:
        num_string(str): number to spell
    Returns:
        str: string with spelled number
    """
    numbers = ['null', 'ein', 'zwei', 'drei', 'vier', 'fünf', 'sechs', 'sieben', 'acht', 'neun', 'zehn',
               'elf', 'zwölf', 'dreizehn', 'vierzehn', 'fünfzehn', 'sechzehn', 'siebzehn', 'achtzehn', 'neunzehn']
    tens = ['null', 'dreizehn', 'zwanzig', 'dreißig', 'vierzig', 'fünfzig', 'sechzig', 'siebzig', 'achtzig', 'neunzig']

    spelling = []
    if int(num_string[0]) != 0:
        spelling.append(numbers[int(num_string[0])] + 'hundert')
    if int(num_string[1]) in [0, 1]:
        spelling.append(numbers[int(num_string[1] + num_string[2])])
    elif int(num_string[1]) > 1:
        spelling.append(numbers[int(num_string[2])] + 'und' + tens[int(num_string[1])])

    return ''.join(spelling)
