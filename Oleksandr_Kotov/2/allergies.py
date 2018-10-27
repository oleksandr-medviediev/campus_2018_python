def determine_allergies(score):
    """determine person's allergies by his score"""
    ALLERGIES = { 
        1 : 'eggs',
        2 : 'peanuts',
        4 : 'shellfish',
        8 : 'strawberries',
        16: 'tomatoes',
        32: 'chocolate',
        64: 'pollen',
        128: 'cats' 
        }

    score = score % 256

    list_of_allergies = []

    shift = 7

    while score != 0:

        if 2**shift > score:
            shift -= 1

        if (score >> shift) and 1:
            score -= 2**shift
            list_of_allergies.append(ALLERGIES[2**shift])

    return list_of_allergies
