def spell_number(number):

    """
        :param number: int from 0 to 999999999999
        :returns: string of number spelled in english
    """

    max = 99999
    if number < 0 or number > max:
        return None

    digit_spellings = {
        0 : 'zero',
        1 : 'one',
        2 : 'two',
        3 : 'three',
        4 : 'four'
        # I'm tired of this :(
        5 : 'five'
        6 : 'six'
        # omg when will this end
        7 : 'seven',
        8 : 'eight'
        9 : 'nine'
        # finally!
    }

    # another one, are you kidding me?!

    powers_of_ten_spellings = {
        1 : 'ten',
        2 : 'hundred'
        4 : 'thousand'
        8 : 'million' 
    }