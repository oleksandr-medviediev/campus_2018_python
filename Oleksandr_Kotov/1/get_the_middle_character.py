my_str = input("type string: ")

center_idx = len(my_str) // 2

if center_idx < len(my_str) / 2:
    print(my_str[center_idx])
else:
    print(my_str[center_idx - 1 : center_idx + 1])