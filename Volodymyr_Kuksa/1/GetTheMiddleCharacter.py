input_string = input("input the string to find out it's middle character(s): ")

center_index = (len(input_string) - 1) // 2

if len(input_string) % 2 != 0:
    print(input_string[center_index])
else:
    print(input_string[center_index:center_index + 2])

