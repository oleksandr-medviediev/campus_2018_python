string = input('enter the string\n')

words_list = string.split()

for i, el in enumerate(words_list):
    words_list[i] = words_list[i].capitalize()

    
string = " ".join(words_list)
print(string)
