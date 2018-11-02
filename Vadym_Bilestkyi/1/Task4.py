def is_isogram(word):
    for letter in word:
        if not letter.isspace() and word.count(letter) > 1:
            return False
    return True


if __name__ == '__main__':
    word = input('Enter word:')
    print(is_isogram(word))
