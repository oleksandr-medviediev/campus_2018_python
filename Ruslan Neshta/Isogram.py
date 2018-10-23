def is_isogram(string):
    isogram = True
    for ch in string:
        if ch.isalpha() and string.count(ch) > 1:
            isogram = False
            break

    return isogram


if __name__ == "__main__":
    phrase = input("Enter a line: ")
    result = is_isogram(phrase)
    print(result)
