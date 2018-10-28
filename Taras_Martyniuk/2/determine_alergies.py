scores = {
    1 : 'eggs',
    2 : 'peanuts',
    4 : 'shellfish',
    8 : 'strawberries',
    16 : 'tomatoes',
    32 : 'chocolate',
    64 : 'pollen',
    128 : 'cats'
}

def determine_allergies(score):

    """
        :param score: int
        :returns: list of all allergies that fit into alergy score
    """

    score = score % 256
    powers_of_2 = [2 ** pow for pow in range(8)]
    powers_of_2.reverse()

    find = lambda pred, iterable : next((x for x in iterable if pred(x)), None)
    res = []

    while score > 0:
        largest_afforable_score = find(lambda x: x <= score, powers_of_2)
        res.append(scores[largest_afforable_score])
        score -= largest_afforable_score

    return res


assert determine_allergies(34) == ["chocolate", "peanuts"]