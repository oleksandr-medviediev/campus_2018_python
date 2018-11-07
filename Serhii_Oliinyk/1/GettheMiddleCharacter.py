def main(string):
    if len(string) % 2 == 0 :
        index = int(len(string) / 2)
        print(string[index : index + 2 : 1])
    else:
        print(string[int(len(string) / 2)])


if __name__ == '__main__':
    main("tesst")
