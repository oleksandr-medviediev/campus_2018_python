
def encode(input_str):
    privios_char = input_str[0]
    semi_char_num = 0
    out_str = ''
    input_str += '.'

    for ch in input_str :
        if ch == privios_char:
            semi_char_num += 1
        else :
            out_str += (str(semi_char_num) if semi_char_num > 1 else '') + privios_char
            privios_char = ch
            semi_char_num = 1
    return out_str


print(encode("WWWBBBBA"))

def decode(input_str):
    num = 0
    out_str = ''

    for ch in input_str:
        if ch.isdigit():
            num = num * 10 + int(ch)
        else:
            out_str += ch * max(num, 1)
            num = 0
    return out_str


print(decode("3W4BA"))
