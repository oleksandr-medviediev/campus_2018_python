

map_units = { 0: '', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine' }
map_ten_to_twenty = { 0 : 'ten' , 1 : 'eleven', 2 : 'twelve', 3 : 'thirteen', 4 : 'fourteen', 5 : 'fifteen', 6 : 'sixteen', 7 : 'seventeen', 8 : 'eighteen', 9 : 'nineteen'}
map_tens = { 2 : 'twenty', 3 : 'thirty', 4 : 'fourty', 5 : 'fifty', 6 : 'sixty', 7 : 'seventy', 8 : 'eighty', 9 : 'ninety'}


word_hundred = 'hundred'
words = ['', 'thousand', 'million', 'billion']
words_iter = 0


def get_tens(number):
    tens = number % 100
    result = ''

    if (tens < 10):
        result = map_units[tens]
    elif (tens < 20):
        result = map_ten_to_twenty[tens % 10]
    else:
        result = map_tens[tens // 10]
        if tens % 10 > 0:
            result += f'-{map_units[tens % 10]}' 
    
    return result



def say_number(number):
    """
    Convert number into a words
    :tparam number: int
    :param number: integer in range(0, 999 999 999 999)
    :rtype: str
    """
    global words_iter
    result = ''
    tmp = ''

    if (number // 1000 > 0):
        words_iter += 1
        tmp = say_number(number // 1000)
        words_iter -= 1
    
    number %= 1000

    result = f'{get_tens(number // 100)} hundred' if number // 100 > 0 else ''
    result += ' and ' if len(result) and number % 100 else ''
    result += get_tens(number)
    result += f' {words[words_iter]} ' if len(result) else ''

    if words_iter == 0 and len(tmp) and number < 100:
        tmp = f'{tmp}and '

    return tmp + result


print(say_number(14))
print(say_number(100))
print(say_number(120))
print(say_number(1002))
print(say_number(1323))
