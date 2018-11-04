numerals_dictionary = {
    0 : 'zero',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen', 
    19 : 'nineteen',
    20 : 'twenty',
    30 : 'thirty',
    40 : 'forty',
    50 : 'fifty',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety',
}


def spell_triade(triade):
    """
    This function returns string, contains correct spelling of input numeric triade
    """
    spelled_triade = ''

    if triade[1] == 1:

        spelled_triade += numerals_dictionary[triade[1] * 10 + triade[2]]

    elif triade[1] == 0:

        spelled_triade += numerals_dictionary[triade[2]]

    else:

        if triade[2] == 0:

            spelled_triade = numerals_dictionary[triade[1] * 10]

        else:

            spelled_triade = '-'.join((numerals_dictionary[triade[1] * 10], numerals_dictionary[triade[2]]))

    if triade[0] in range(1, 10):

        hundreds = ' '.join((numerals_dictionary[triade[0]], 'hundred'))

        if spelled_triade != 'zero':

            spelled_triade = ' and '.join((hundreds, spelled_triade))

        else:

            spelled_triade = hundreds

    return spelled_triade
