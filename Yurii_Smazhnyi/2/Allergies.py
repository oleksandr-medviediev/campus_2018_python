allergies_list = ["eggs", "peanuts", "shellfish", "strawberies", "tomatoes", "chocolate", "pollen", "cats"]


def get_allergies_list(score):

    """
    Takes score of allergies and returns allergy list instead

    @param score: allergy score
    @returns: list of allergies
    """

    allergies = []
    current_score = score

    start_index = len(allergies_list) - 1

    for i in range(start_index, -1, -1):

        score_for_allergy = 1 * (2 ** i)

        if(current_score >= score_for_allergy):

            current_score = current_score % score_for_allergy

            allergies.append(allergies_list[i])
    
    return allergies


print(get_allergies_list(71))
