def main(string):
    result = True

    if string.find(":") == -1:
        result = False

    array = string.split(":")

    if (not array[0].isdigit()) or (not array[1].isdigit()):
        result = False

    if (int(array[0]) < 0) or (int(array[0]) > 23):
        result = False

    if (int(array[1]) < 0) or (int(array[1]) > 59):
        result = False

    return result


if __name__ == '__main__':
    result = main("10:50")
    print(result)
