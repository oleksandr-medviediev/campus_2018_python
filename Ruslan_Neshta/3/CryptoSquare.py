import math


def normalize(string):
    """
    Removes all non-alphabetic symbols and translates text into lowercase

    :param string: text

    :return: normalized text
    :rtype: str
    """

    normalized = []

    for ch in string:
        if ch.isalpha():
            normalized.append(ch.lower())

    target = "".join(normalized)
    return target


def form_square(string):
    """
    Form crypto square

    :param string: text

    :return: list of strings
    :rtype: list
    """

    result = []
    normal_string = normalize(string)
    root = math.sqrt(len(normal_string))

    rows = math.floor(root)
    columns = math.ceil(root)

    word = []
    counter = 0
    for i in range(len(normal_string)):

        if counter < columns:
            word.append(normal_string[i])
            counter += 1
        else:
            result.append("".join(word))
            word = [normal_string[i]]
            counter = 1

    result.append("".join(word))
    return result


if __name__ == "__main__":
    words = "If man was meant to stay on the ground, god would have given us roots."
    res = form_square(words)
    print(*res, sep="\n")
