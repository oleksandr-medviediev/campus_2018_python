number_names = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

tens_names = {
    2: 'twenty',
    3: 'thirty',
    4: 'fourty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}

def say_number_up_to_thousand(number):

    """ Function return string view of number in range [0, 999]

        Args:
            number(int): number from 0 to 999 including

        Returns:
            str: string which view this number

    """
    
    if number // 1000 > 0:
        return AssertionError("Invalid using")
    
    word_list = []

    hundreds_count = number // 100
    number %= 100

    if hundreds_count > 0:
        word_list.append(number_names[hundreds_count])
        word_list.append('hundred')
        
        if number > 0:
            word_list.append('and')

    if number < 20:
        word_list.append(number_names[number])
    else:
        tens_count = number // 10
        word_list.append(tens_names[tens_count])
        number %= 10
        word_list.append(number_names[number])

    number_string = " ".join(word_list)

    return number_string.strip()

    
def say_number(number):


    """ Function return string view of number in range [0, 999999999999]

        Args:
            number(int): number from 0 to 999999999999 including

        Returns:
            str: string which view this number

    """

    if number == 0:
        return 'zero'
    
    limit_range = 10 ** 9

    range_names = ['billion',
                   'million',
                   'thousand',
                   '']
    word_list = []

    range_counter = 0
    
    while number > 0:
        range_value = number // limit_range
        if range_value > 0:
            word_list.append(say_number_up_to_thousand(range_value))
            word_list.append(range_names[range_counter])

        number %= limit_range
        limit_range /= 10 ** 3

        range_counter += 1

    result_string = ' '.join(word_list)
    
    return result_string.strip()
