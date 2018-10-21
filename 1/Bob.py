phrase = input("say smth to Bob\n")

if phrase.upper() == phrase:
    print("Whoa, chill out!")
elif phrase[len(phrase)-1] == '?':
    print("Sure.")
elif len(phrase.strip()) == 0:
    print("Fine. Be that way!")
else:
    print("Whatever.")
    
input()