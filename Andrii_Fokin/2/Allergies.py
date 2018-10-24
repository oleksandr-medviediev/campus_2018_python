import sys
def determine_allergies(score):
    allergens = ["eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"]
    iters = filter(lambda x: score >> x & 1, range(len(allergens)))
    return map(lambda x: allergens[x], iters)


print(*determine_allergies(0))