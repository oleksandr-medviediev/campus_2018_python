string = input("Enter string \n")
string.lower()

used_letters = ""

succeed = True

for char in string:
    if used_letters.find(char) == -1:
        used_letters += char
    elif char.isspace() or char == "_":
        continue;
    else:
        succeed = False
        break;

print(succeed)
