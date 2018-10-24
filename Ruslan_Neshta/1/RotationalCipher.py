def rotational_cipher(string, number):
    letters = []
    for ch in string:
        letters.append(chr(ord(ch) + number))
    return str.join("", letters)


if __name__ == "__main__":
    line = input("Enter a string: ")
    amount = input("Enter a number: ")
    print(rotational_cipher(line, int(amount)))
