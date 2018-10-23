def is_same_x_as_o(string):
    line = string.lower()
    return line.count('x') == line.count('o')


if __name__ == "__main__":
    phrase = input("Enter a line: ")
    result = is_same_x_as_o(phrase)
    print(result)