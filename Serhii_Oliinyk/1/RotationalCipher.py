def main(key, string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    list = []
    list.extend(string)

    for i in range(len(list)):
        index = alphabet.find(string[i])
        index += key

        if(index >= len(alphabet)):
            index = index - len(alphabet)

        list[i] = alphabet[index]

    string = "".join(list)

    return string


if __name__ == '__main__':
    result = main(1, "abc")
    print(result)
