def spell_number(number):
    """
        :param number: int from 0 to 999999999
        :returns: string of number spelled in english
    """   
    max = 999999999
    if number < 0 or number > max:
        return None

    digit_spellings = {
        0 : 'zero',
        1 : 'one',
        2 : 'two',
        3 : 'three',
        4 : 'four',
        # I'm tired of this :(
        5 : 'five',
        6 : 'six',
        # omg when will this end
        7 : 'seven',
        8 : 'eight',
        9 : 'nine'
        # finally!
    }

    powers_of_two = [1, 2, 3, 6]
    tens_powered = [10 ** pow for pow in powers_of_two]

    # another one, are you kidding me?!
    tens_powered_spellings = {
        10 : 'ten',
        100 : 'hundred',
        1000 : 'thousand',
        1000000 : 'million'
    }

    for ten_pow in tens_powered[::-1]:
        ten_pow_count = 0
        while number >= ten_pow:
            number -= ten_pow
            ten_pow_count += 1
        
        assert ten_pow_count >= 0 and ten_pow_count < 1000
        if ten_pow_count > 0:
            if ten_pow == 10:
                # yes, 'fivety' is not exactly what i need, but i couldnt do yet another hardcoded map
                print(f'{digit_spellings[ten_pow_count]}ty')
            else:
                print(f'{ten_pow_count} {tens_powered_spellings[ten_pow]}')

    assert number < 10
    if number > 0:
        print(f'and {digit_spellings[number]}')

spell_number(999999999)

# 999 million
# 999 thousand
# 9 hundred
# ninety
# and nine
