def encode(input_str):
    """RLE encoder
    
    Arguments:
        input_str {str} -- string to encode like "AWWWBBBBA"

    Returns:
        result {str} -- encoded string like "A3W4BA"
    """
    privios_char = input_str[0]
    semi_char_num = 0
    result = ""

    for i in input_str:
        if i == privios_char:
            semi_char_num += 1
        else:
            if semi_char_num > 1:
                result += str(semi_char_num)
            result += privios_char
            privios_char = i
            semi_char_num = 1
    return result


def decode(input_str):
    """RLE decoder
    
    Arguments:
        input_str {str} -- encoded string like "A3W4BA"

    Returns:
        result {str} -- decoded string like "AWWWBBBBA"
    """
    num = 0
    result = ""

    for i in input_str:
        if i.isdigit():
            num = num * 10 + int(i)
        else:
            result += i * max(num, 1)
            num = 0
    return result


print(encode("AWWWBBBBA"))
print(decode("A3W4BA"))
