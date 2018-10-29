
def determine_allergies(score):
    """function 

    Arguments:
        score {integer} -- score of alergies

    Returns:
        list -- list of things that are person is alergic to
    """
    allergens = ["eggs", "peanuts", "shellfish", "strawberries",
                 "tomatoes", "chocolate", "pollen", "cats"]

    filter_function = lambda x: score >> x & 1

    iters = filter(filter_function, range(len(allergens)))
    result = list(map(lambda x: allergens[x], iters))
    return result


print(determine_allergies(257))
print(determine_allergies(34))
