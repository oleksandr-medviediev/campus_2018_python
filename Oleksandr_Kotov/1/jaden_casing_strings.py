my_str = input("type phrase: ")

words = my_str.split()

new_str = ""

for i in range(0, len(words)):
    words[i] = words[i].capitalize()
    new_str += words[i] + ' '
    
print(new_str)
