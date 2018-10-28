<<<<<<< HEAD
print("Determine if a word or phrase is an isogram.")

user_input = input("Enter string: ")

char_count_in_string = 0
is_isogram = True

for x in user_input:

    if x.isalpha() == True:
        char_count_in_string = user_input.count(x)

        if char_count_in_string > 1:
            is_isogram = False
            break
    
print(is_isogram)
=======
print("Determine if a word or phrase is an isogram.")

user_input = input("Enter string: ")

char_count_in_string = 0
is_isogram = True

for x in user_input:

    if x.isalpha() == True:
        char_count_in_string = user_input.count(x)

        if char_count_in_string > 1:
            is_isogram = False
            break
    
print(is_isogram)
>>>>>>> 715fd0763b415a13fb28a483f258a5eadc1ec931
