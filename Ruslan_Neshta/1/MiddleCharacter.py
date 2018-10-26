def get_middle_character(string):
    first = int(len(string) / 2)
    second = first + 1

    if len(string) % 2 == 0:
        first -= 1

    return string[first:second]


if __name__ == "__main__":
    phrase = input("Enter a line: ")
    result = get_middle_character(phrase)
    print(result)
