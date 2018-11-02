allergies = {
    1: 'eggs',
    2: 'peanuts',
    4: 'shellfish',
    8: 'strawberries',
    16: 'tomatoes',
    32: 'chocolate',
    64: 'pollen',
    128: 'pollen'
}


def determine_allergies(allergies_score):
    result = []
    for score, allergy in allergies.items():
        if allergies_score & score:
            result.append(allergy)

    return result


print(determine_allergies(257))
print(determine_allergies(34))
print(determine_allergies(0))
