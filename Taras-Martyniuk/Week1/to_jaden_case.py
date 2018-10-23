words = input().split(' ')
cap_words =  map(lambda x : x.capitalize(), words)
print(' '.join(cap_words))