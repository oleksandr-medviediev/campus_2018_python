input_string = input('Enter a string\n')

string_size = len(input_string)

for i in range((string_size - 1)//2, string_size//2 + 1):
    print(input_string[i], end = '')
