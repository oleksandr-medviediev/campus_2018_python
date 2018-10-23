def reverse_string(string):
    return string[::-1]


if __name__ == "__main__":
    line = input("Enter a line: ")
    result = reverse_string(line)
    print(result)
