def determine_allergies(allergy_score):
    """
    Return list of allergies, determined by allergy_score.

    :param allergy_score: sum of all allergy scores.
    :type allergy_score: int

    :return: list of allergy names.
    :rtype: list.
    """
    allergy_names = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats']
    allergy_values = [1, 2, 4, 8, 16, 32, 64, 128]

    result = []

    for i in range(len(allergy_names)):

        if allergy_score & allergy_values[i]:

            result.append(allergy_names[i])

    return result


print(determine_allergies(34))
print(determine_allergies(257))
