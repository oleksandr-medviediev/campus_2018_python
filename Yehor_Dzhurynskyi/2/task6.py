allergies = (
    'eggs',
    'peanuts',
    'shellfish',
    'strawberries',
    'tomatoes',
    'chocolate',
    'pollen',
    'cats'
)


def determine_allergies(mask):

    mask = mask & 255

    determined_allergies = [allergies[i] for i in range(len(allergies)) if mask & (1 << i)]

    return determined_allergie
