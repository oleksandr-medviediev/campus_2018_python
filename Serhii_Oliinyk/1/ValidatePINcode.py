def main(string):
    result = True

    if (len(string) != 4) and (len(string) != 6):
        result = False

    result = string.isdigit()

    return result


if __name__ == '__main__':
    result = main("1234")
    print(result)
