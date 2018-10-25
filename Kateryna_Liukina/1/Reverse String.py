input_string = input('Enter a string\n')

for i in range(len(input_string) - 1, -1, -1):
    print(input_string[i], end = '')