<<<<<<< HEAD
print("Return the middle character of the word.")
print("If the word's length is odd, return the middle character.")
print("If the word's length is even, return the middle 2 characters.")

user_input = input("Enter string: ")

user_input_len = len(user_input)

output = str()

if user_input_len % 2 == 0:
    
    first_middle = user_input_len // 2 - 1
    second_middle = user_input_len // 2

    output += user_input[first_middle]
    output += user_input[second_middle]
    
else:
    output += user_input[user_input_len // 2]

print(output)
=======
print("Return the middle character of the word.")
print("If the word's length is odd, return the middle character.")
print("If the word's length is even, return the middle 2 characters.")

user_input = input("Enter string: ")

user_input_len = len(user_input)

output = str()

if user_input_len % 2 == 0:
    
    first_middle = user_input_len // 2 - 1
    second_middle = user_input_len // 2

    output += user_input[first_middle]
    output += user_input[second_middle]
    
else:
    output += user_input[user_input_len // 2]

print(output)
>>>>>>> 715fd0763b415a13fb28a483f258a5eadc1ec931
