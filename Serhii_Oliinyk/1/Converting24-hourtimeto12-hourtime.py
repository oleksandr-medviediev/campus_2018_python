def main(string):
    result = ""

    if string.find(":") == -1:
        result = "not a valid time"

    array = string.split(":")

    if (not array[0].isdigit()) or (not array[1].isdigit()):
        result = "not a valid time"

    if (int(array[0]) < 0) or (int(array[0]) > 23):
        result = "not a valid time"

    if (int(array[1]) < 0) or (int(array[1]) > 59):
        result = "not a valid time"

    if result == "not a valid time":
        return result

    if int(array[0]) >= 12:
        result += "0" + str((int(array[0]) -  12)) + ":" + array[1] + " pm"
    else:
        result += array[0] + ":" + array[1] + " am"

    return result


if __name__ == '__main__':
    result = main("25:20")
    print(result)
