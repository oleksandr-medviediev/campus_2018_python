allergies = { 
    1: "eggs",
    2: "peanuts",
    4: "shellfish",
    8: "strawberries",
    16: "tomatoes",
    32: "chocolate",
    64: "pollen",
    128: "cats",
    }


def determine_allergies(score):
    """
    Detects all allergies by given score.

    Args:
        score (int): score.

    Returns:
        List of str.
    """
    res = []
    for i in allergies:
        print(bin(i & score))
        if bin(i & score) == bin(i):
            res.append(allergies[i])
    return res


print(determine_allergies(34))
