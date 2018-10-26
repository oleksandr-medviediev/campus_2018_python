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

    result = list()

    for key in allergies: 
        
        if key & allergies_score: result.append(allergies.get(key))

    if len(result): return result
    else: return "None"

import random
print(determine_allergies(random.randrange(1024)))
