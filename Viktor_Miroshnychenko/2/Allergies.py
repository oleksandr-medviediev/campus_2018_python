def find_allergis(total_score):
    """
    :param total_score: total score of allergies
    :type total_score: int

    :return: list of allergies
    :rtype: list
    """
    aler_score = [1, 2, 4, 8, 16, 32, 64, 128]
    aler_names = ["eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"]
    aler_score.reverse()
    aler_names.reverse()

    return_val = []
    for pos in range(len(aler_score)):
        if aler_score[pos] <= total_score:
            return_val.append(aler_names[pos])
            total_score -= aler_score[pos]

    return return_val


print(find_allergis(93))
    
