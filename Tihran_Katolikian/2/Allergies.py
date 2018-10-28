def determine_allergies(score):
    """
    Method helps to find a list of dangerous food for Tom according to an allergic score
    :param score: an allergic score
    :return:  the list of dangerous products for Tom according to score
    """
    allergic_map = {
        'eggs': 1,
        'peanuts' : 2,
        'shellfish' : 4,
        'strawberries' : 8,
        'tomatoes' : 16,
        'chocolate' : 32,
        'pollen' : 64,
        'cats' : 128
    }

    # I don't understand how it should work. I will do it later
