def main(string):
    xCount = oCount = 0

    xCount += string.count('x')
    xCount += string.count('X')

    oCount += string.count('o')
    oCount += string.count('O')
    
    print(xCount == oCount)


if __name__ == '__main__':
    main("ooxx")
