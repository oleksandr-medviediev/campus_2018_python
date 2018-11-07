def main(string):
    result = True

    if string == "":
        result = False

    for i in string:
        if string.count(i) > 1:
            result = False

    return True


if __name__ == '__main__':
    result = main("abolishment")
    print(result)
