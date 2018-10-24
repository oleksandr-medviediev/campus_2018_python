def determine_allergies(num):
    """
    An allergy test produces a single numeric score which contains the information about all the allergies the person has.

    :param num: integer - sum of scores of person allergies
    :return: list of allergens names
    :rtype: list
    """

    scores = [
        ('eggs', 1),
        ('peanuts', 2),
        ('shellfish', 4),
        ('strawberries', 8),
        ('tomatoes', 16),
        ('chocolate', 32),
        ('pollen', 64),
        ('cats', 128)
    ]

    num = num % 256  
    res = []

    for el in reversed(scores):
        
        if num >= el[1]:
            num -= el[1]
            res.append(el[0])
    
    return res


if __name__ == "__main__":
    result = determine_allergies(280)
    print(result)
