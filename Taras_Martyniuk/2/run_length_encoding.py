from itertools import groupby


def group_encode(char, group):

    """
        :param char: char
        :param group: iterable
        :returns: string in format "{char}{length of iterable}"
    """

    len_str = str(len(list(group)))
    return char + len_str


def run_length_encode(string):

    """
        :param string: a string
        :returns: string where each subsequent group of same chars is represented 
            by char followed by number of occurences
    """

    group_str_list = [group_encode(char, group) for char, group in groupby(string)]
    return "".join(group_str_list)


def pairwise(iterable):

    """
        :returns: iterator over iterable that yields 2 elements at a time
    """

    a = iter(iterable)
    return zip(a, a)


def decode(string):

    """
        :param: run-length encoded string
        :return: original string
    """

    res = []

    char_digits_groups = groupby(string, lambda x : x.isdigit())
    char_times_strs = [ "".join(list(group)) for _, group in char_digits_groups ]

    for char, times_encountered_str in pairwise(char_times_strs):
        assert times_encountered_str.isdigit()

        times_encountered = int(times_encountered_str)
        res.append(char * times_encountered)

    return "".join(res)

original = "H" * 10 + "W" * 20 + "H" * 10
encoded = "H10W20H10"
assert run_length_encode(original) == encoded
assert decode(encoded) == original


