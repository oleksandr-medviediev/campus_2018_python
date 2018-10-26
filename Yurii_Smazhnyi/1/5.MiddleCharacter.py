string = input("input your string: ")

str_len = len(string)

if str_len != 0:
    is_even = str_len % 2 == 0
    index = str_len // 2

    if is_even: 
        print(string[index - 1] + string[index])

    else:
        print(string[index])
