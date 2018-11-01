def determine_allergies(allergy_score):
    """
    Determines alergies of a person with a given score

Args:
    allergy_score (int) integer score of all allergens

Returns:
    list of allergies person with a given score has
    """

    allergies = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chockolate', 'pollen', 'cats']

    person_allergies = []

    for i in range(len(allergies)):
        if allergy_score == 0:
            break
        elif allergy_score % 2:
            person_allergies.append(allergies[i])

        allergy_score //= 2

    return person_allergies
