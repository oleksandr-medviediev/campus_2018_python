string = input('Enter string: ')

words = string.split()
for i in range(len(words)):
    if i != 0:
        print(' ', end='')

    print(str.capitalize(words[i]), end = '')

print()
