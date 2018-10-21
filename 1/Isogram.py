word = input("enter a word\n")

words = word.split(" ")

if len(words) > 1:
    print("There are many words")

for wrd in words:
    word_set = set()
    for i in wrd.lower():
        if i in word_set:
            print(wrd + " = false")
            break
        else:
            word_set.add(i)
    else:
        print(wrd + " = true")
input()