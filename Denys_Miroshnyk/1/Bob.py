phrase = input("say smth to Bob\n")

if phrase == "":
    print("Fine. Be that way!")
elif phrase[-1] == '?':
    print("Sure.")
elif phrase.upper() == phrase:
    print("Whoa, chill out!")
else:
    print("Whatever.")
    
input()
