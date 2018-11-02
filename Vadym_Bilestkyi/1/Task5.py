def get_middle(word):
    word_len = len(word)
    is_even = (word_len % 2 == 0)

    middle_start = word_len // 2 - (1 if is_even else 0)
    middle_end = word_len // 2 + 1

    return word[middle_start:middle_end]


print(get_middle('test'))
print(get_middle('testing'))
