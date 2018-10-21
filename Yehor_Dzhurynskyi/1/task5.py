string = input('Enter string: ')

center_idx = len(string) // 2
has_even_len = len(string) % 2 == 0

if has_even_len:
    print(string[center_idx - 1: center_idx + 1])
else:
    print(string[center_idx])
