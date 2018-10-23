text = input('input text:\n')

text = text.strip()

if len(text) == 0:
    print( "Fine. Be that way!")
else:
    isQuestion = text[len(text) - 1] == '?'
    isUppercase = text.isupper()

    if isQuestion and isUppercase:
        print("Calm down, I know what I'm doing!")
    elif isQuestion and not isUppercase:
        print("Sure.")
    elif not isQuestion and isUppercase:
        print( "Whoa, chill out!")
    else:
        print("Whatever.")
