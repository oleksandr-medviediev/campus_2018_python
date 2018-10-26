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
    """
    determine which allergies coded in bit mask
        :param mask: integer bit mask of allergies
        :return: collection of allergy names
    """

    mask = mask & 255

    determined_allergies = [allergies[i] for i in range(len(allergies)) if mask & (1 << i)]

    return determined_allergie
