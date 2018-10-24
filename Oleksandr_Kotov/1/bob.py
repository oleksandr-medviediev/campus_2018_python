while True:
    phrase = input("talk to Bob: ")

    if len(phrase) == 0:
        print("Fine. Be that way!")

    elif phrase[-1] == '?' and phrase.isupper():
        print("Calm down, I know what I'm doing!")

    elif phrase[-1] == '?':
        print("Sure.")

    elif phrase.isupper():
        print("Whoa, chill out!")

    else:
        print("Whatever.")