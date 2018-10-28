def determine_allergies(score):

    #ignore some allergens
    score %= 256
    
    if score == 0:
        return None

    allergies = []
    
    if score >= 128:
        score -= 128
        allergies.append('cats')

    if score >= 64:
        score -= 64
        allergies.append('pollen')

    if score >= 32:
        score -= 32
        allergies.append('chocolate')

    if score >= 16:
        score -= 16
        allergies.append('tomatoes')

    if score >= 8:
        score -= 8
        allergies.append('strawberries')

    if score >= 4:
        score -= 4
        allergies.append('shellfish')

    if score >= 2:
        score -= 2
        allergies.append('peanuts')

    if score == 1:
        allergies.append('eggs')

    allergies.reverse()
    
    return allergies
