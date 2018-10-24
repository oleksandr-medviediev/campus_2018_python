def encode(in_string):
    res = ''
    curr_len = len(in_string)
    while (curr_len > 0):
        prev_len = curr_len
        symbol = in_string[0]
        in_string = in_string.lstrip(symbol)
        curr_len = len(in_string)
        occurrence_count = prev_len - curr_len
        if occurrence_count != 1:
            res += str(occurrence_count)
        res += symbol
    return res


def decode(in_string):
    res = ''
    n = 0
    for ch in in_string:
        if ch.isalpha():
            res += ch * max(1, n)
            n = 0
        else:
            n = n * 10 + int(ch)
    return res

print(decode("32AB3CD4E"))
