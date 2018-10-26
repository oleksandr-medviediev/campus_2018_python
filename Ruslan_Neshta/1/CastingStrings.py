def cast_strings(string):
    strings = []
    for line in string.split(' '):
        strings.append(line.title())
        strings.append(' ')

    return str.join("", strings)


if __name__ == "__main__":
    phrase = input("Enter a line: ")
    result = cast_strings(phrase)
    print(result)
