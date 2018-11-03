def spell_number(number):
    """
    This function allows to spell the input number in English.
    :param number: the number to spell
    :type number: int
    :return: the spelling of the input number
    :rtype: str
    """
    if number == 0:
        return "zero"
    numeric_order = [""," thousand ", " million ", " billion "]
    output = str()
    while number > 0:
        number,part = divmod(number,1000)
        if part > 0:
            output = ''.join([spell_number_under_thousand(part),numeric_order[0],output])
        numeric_order.pop(0)

    return output

def spell_number_under_thousand(number):
    """
    This function allows to spell the number lessthan thousand by pattern in English.
    :param number: the number to spell
    :type number: int, less than 1000
    :return: the spelling of the input number
    :rtype: str
    """
    less_twenty_map = {
                  1:"one",
                  2:"two",
                  3:"three",
                  4:"four",
                  5:"five",
                  6:"six",
                  7:"seven",
                  8:"eight",
                  9:"nine",
                  10:"ten",
                  11:"eleven",
                  12:"twelve",
                  13:"thirteen",
                  14:"fourteen",
                  15:"fifteen",
                  16:"sixteen",
                  17:"seventeen",
                  18:"eighteen",
                  19:"nineteen"
                  }
    
    tenth_map = {
        2:"twenty",
        3:"thirty",
        4:"fourty",
        5:"fifty",
        6:"sixty",
        7:"seventy",
        8:"eighty",
        9:"ninety"
        }
    
    suffixes = [ " ", " and "]
    answer = str()
    
    hundred_part = number // 100
    tenth_part, part = divmod(number % 100, 10)
    suffix_index = 0 if number % 100 == 0 else 1
    
    if hundred_part > 0:
        var1 = less_twenty_map[hundred_part]
        var2 = suffixes[suffix_index]
        answer = f'{var1} hundred {var2}'
    if tenth_part in tenth_map:
        var = tenth_map[tenth_part]
        answer = ''.join([answer,f'{var} '])
    if part in less_twenty_map:
        var = less_twenty_map[part]
        answer = ''.join([answer,f'{var}'])

    if number == 10:
        var = less_twenty_map[number]
        answer = ''.join([answer,f'{var}'])
        
    return answer


if __name__ == "__main__":

    validation = False
    while not validation:
        
        number = input("Your number\n")
        validation = number.isnumeric()
        if validation:
            number = int(number)
            
    print(spell_number(number))
