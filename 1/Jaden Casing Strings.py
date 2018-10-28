words = input("enter string\n").split(" ")
jaden_cased = []

for word in words:
    title_cased = word[0].upper() + word[1:]
    jaden_cased.append(title_cased)

new_string = ""

for word in jaden_cased:
    new_string += word + " "

print(new_string.strip())
input()