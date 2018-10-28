word = input("enter a word\n")

words = word.split(" ")

if len(words) > 1:
    print("There are many words")

for wrd in words:
    is_isogram = len(wrd) == len(set(wrd))
    is_isogram = wrd + " " + str(is_isogram)
    print(is_isogram)
   
input()
