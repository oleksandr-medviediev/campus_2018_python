"""
This script solves task 2.6 from Coding Campus 2018 Python course
(Allergies)
"""

import math


allergies = {
    1: "Eggs",
    2: "Peanuts",
    4: "Shellfish",
    8: "Strawberries",
    16: "Tomatoes",
    32: "Chocolate",
    64: "Pollen",
    128: "Cats"
}


def determine_allergies(score):
    """
    Determine person's allergies based on score
    :param score: Allergy score value
    :return: List containing allergy names
    """

    return_list = []
    power = int(math.log2(score))

    if power > 7:
        score -= 2 ** power

    for key in reversed(list(allergies.keys())):

        if score / key >= 1:

            return_list.append(allergies[key])
            score -= key

    return return_list
