import random


def determine_allergies(allergies_score):
    """
        This function checks allergies by simple bitwise masking
    """
    allergies = {
        1: "eggs",
        2: "peanuts",
        4: "shellfish",
        8: "strawberries",
        16: "tomatoes",
        32: "chocolate",
        64: "pollen",
        128: "cats"
    }

    result = [allergies.get(key) for key in allergies if key & allergies_score]

    return result or None


print(determine_allergies(random.randrange(1024)))
