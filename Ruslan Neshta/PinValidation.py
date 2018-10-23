def validate_pin(string):
    is_valid = False

    if len(string) == 4 or len(string) == 6:
        is_valid = string.isdigit()

    return is_valid


if __name__ == "__main__":
    phrase = input("Enter a time in 24 hour format: ")
    result = validate_pin(phrase)
    print(result)
