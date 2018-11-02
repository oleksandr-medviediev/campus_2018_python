def is_same_amount_of_oxs(word):
    word = word.lower()
    return word.count('x') == word.count('o')


print(is_same_amount_of_oxs('ooxx'))
print(is_same_amount_of_oxs('xooxx'))
print(is_same_amount_of_oxs('ooxXm'))
print(is_same_amount_of_oxs('zpzpzpp'))
