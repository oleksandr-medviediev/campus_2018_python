from math import floor


little_numbers = {
    0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',\
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',\
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',\
    18: 'eighteen', 19: 'nineteen'
}


tens = {
    20: 'twenty', 30: 'thirty', 40: 'fourty', 50: 'fifty', 60: 'sixty', 70: 'seventy',\
    80: 'eighty', 90: 'ninety'
}


def get_string_representation_to_100(number):
    '''
    This function returns a string representation of number in range (0, 99)
    :param number: a number in range(0, 99)
    :return: a string representation of this number
    :type number: int
    :rtype: list of strings
    '''
    string_representation = []

    if number in range(20, 100):
        string_representation.append(tens[(number // 10) * 10])
        string_representation.append(little_numbers[number % 10])
    else:   # simplest case
        string_representation.append(little_numbers[number])

    return string_representation


def get_string_representation_to_1000(number):
    '''
    This function returns a string representation of number in range (0, 999)
    :param number: a number in range(0, 999)
    :return: a string representation of this number
    :type number: int
    :rtype: list of strings
    '''
    string_representation = []

    number_of_hundreds = number // 100
    number %= 100

    if number_of_hundreds > 0:
        string_representation.extend([little_numbers[number_of_hundreds], 'hundred'])
        if number > 0:
            string_representation.append('and')

    string_representation.extend(get_string_representation_to_100(number))

    return string_representation

    
def say_number(number):
    '''
    I really don't like this task!
    This function returns a string representation of number up to 999999999999
    :param number: a number
    :return: a string representation of number
    :type number: int
    :rtype: string
    '''

    ranges = [10 ** 9, 10 ** 6, 10 ** 3, 10 ** 0]
    range_names = ['billion', 'million', 'thousand', '']
    range_counter = 0
    
    string_representation = []
    
    while number:
        current_range = number // ranges[range_counter]
        if current_range > 0:
            string_representation.extend(get_string_representation_to_1000(current_range))
            string_representation.append(range_names[range_counter])
            number %= ranges[range_counter]
        range_counter += 1

    resulting_string = ' '.join(string_representation)

    return resulting_string.strip()
