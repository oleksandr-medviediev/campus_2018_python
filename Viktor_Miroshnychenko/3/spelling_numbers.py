DIGIT_SPELLING = {0:"", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
DECADES_SPELLING = {2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}
SECOND_DECADE = {10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"forteen", 15:"fifteen",16:"sixteen", 17:"forteen", 18:"eighteen", 19:"nineteen"}


def spell_digit(number):
    """
    :param number: number to spell
    :type number: int

    :return: spelled number
    :rtype: str    
    """

    if number == 0:
        return ""
    
    spell = " " + DIGIT_SPELLING[number]

    return spell


def spell_decade(number):
    """
    :param number: number to spell
    :type number: int

    :return: spelled number
    :rtype: str    
    """

    spell = ""
    if number > 19:
        spell += DECADES_SPELLING[number//10]
        spell += spell_digit(number%10)
    else:
        spell = SECOND_DECADE[number]

    return spell



def spell_hundreds(number):
    """
    :param number: number to spell
    :type number: int

    :return: spelled number
    :rtype: str    
    """

    spell = spell_digit(number//100)
    if spell != "":
        spell += " hundred "
    spell += spell_decade(number%100)

    return spell


def spell_thousend(number):
    """
    :param number: number to spell
    :type number: int

    :return: spelled number
    :rtype: str    
    """

    spell = spell_hundreds(number//1000) + " thousends "
    spell += spell_hundreds(number%1000)

    return spell



def spell_milion(number):
    """
    :param number: number to spell
    :type number: int

    :return: spelled number
    :rtype: str    
    """

    spell = spell_hundreds(number // 1000000) + " milion"
    spell += spell_thousend(number%1000000)

    return spell

    


def spell_number(number):
    """
    :param number: number to spell
    :type number: int

    :return: spelled number
    :rtype: str    
    """

    spell = ""
    if number > 1000000:
        spell = spell_milion(number)
    elif number > 1000:
        spell = spell_thousend(number)
    elif number > 100:
        spell = spell_hundreds(number)
    elif number > 10:
        spell = spell_decade(number)
    else:
        spell = spell_digit(number)

    return spell


print(spell_number(2))
print(spell_number(25))
print(spell_number(432))
print(spell_number(85863))
print(spell_number(475937511))
print(spell_number(23456))

