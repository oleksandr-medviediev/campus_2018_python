def main(string):
    result = ""

    array = string.split(" ")
    for i in array:
        result += i.capitalize() + " "

    print(result)


if __name__ == '__main__':
    main("hello world")
