sentence = input("Enter string (more then one word is preffered) \n")
jaden_style_copy = ""

last_letter = " "
for char in sentence:
    if last_letter == " ":
        jaden_style_copy += char.upper()
    else:
        jaden_style_copy += char

    last_letter = char

print(jaden_style_copy)
