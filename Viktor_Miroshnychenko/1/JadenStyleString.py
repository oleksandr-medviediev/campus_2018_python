sentence = input("Enter string (more then one word is preffered) \n")
jaden_style_copy = ""

last_letter = " "
for iter in range(len(sentence)):
    if last_letter == " ":
        jaden_style_copy += sentence[iter].upper()
    else:
        jaden_style_copy += sentence[iter]

    last_letter = sentence[iter]


print(jaden_style_copy)
