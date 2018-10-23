from itertools import groupby

def group_encode(char, group):

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
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)

def decode(string):

    """
        :param: run-length encoded string
        :return: original string
    """

    res = []

    char_digits_groups = groupby(string, lambda x : x.isdigit())

    for char_pair, digit_pair in char_digits_groups:
        print(char_pair[0])
        print(list(char_pair[1]))

        print(digit_pair[0])
        print(list(digit_pair[1]))

    # for i in range(0, len(string), 2):
    #     char = string[i]
    #     times_present = int(string[i + 1])
    #     res.append(char * times_present)

    return "".join(res)

original = "H" * 10 + "W" * 20 + "H" * 10
encoded = "H10W20H10"
assert run_length_encode(original) == encoded

print(decode(encoded))


