str = input("enter string\n")

middle_index = int(len(str)/2)

if len(str) % 2 == 0:
    print(str[middle_index - 1 : middle_index + 1])
else:
    print(str[middle_index])
input()