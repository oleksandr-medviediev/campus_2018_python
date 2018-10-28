from itertools import groupby


def find_the_odd(list_of_int):

    list_of_str = [str(i) for i in list_of_int]
    string_of_int = "".join(list_of_str)
    for ch in string_of_int:
        if string_of_int.count(ch) % 2:
            return int(ch)


def find_the_odd2(list_of_int):

    list_of_int.sort()
    list_of_str = [str(i) for i in list_of_int]
    string_of_int = "".join(list_of_str)
    for ch,l in groupby(string_of_int):
        if len(list(l)) % 2:
            return int(ch)

