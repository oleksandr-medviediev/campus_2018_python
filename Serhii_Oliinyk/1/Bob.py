def main(string):
    result = ""

    if string == "":
        result = "Fine. Be that way!"
    elif string.isupper() and (string[len(string) - 1] == "?"):
        result = "Calm down, I know what I'm doing!"
    elif string.isupper():
        result = "Whoa, chill out!"
    elif string[len(string) - 1] == "?":
        result = "Sure."
    else:
        result = "Whatever."

    return result


if __name__ == '__main__':
    result = main("How are you")
    print(result)
