print("Determine if a word or phrase is an isogram.")

user_input = input("Enter string: ")

count = 0

for x in user_input:
    if x.isalpha() == True:
        count = user_input.count(x)

        if count > 1:
            print(False)
            break

if count == 0:
    print(False)
    
elif count == 1:
    print(True)