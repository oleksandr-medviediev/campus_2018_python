def is_same_amount_of_oxs(word):
    word = word.lower()
    is_same_amount = (word.count('x') == word.count('o'))
    return is_same_amount


print(is_same_amount_of_oxs('ooxx'))
print(is_same_amount_of_oxs('xooxx'))
print(is_same_amount_of_oxs('ooxXm'))
print(is_same_amount_of_oxs('zpzpzpp'))
