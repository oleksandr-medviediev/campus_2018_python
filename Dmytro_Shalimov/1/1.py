<<<<<<< HEAD
print("Check to see if a string has the same amount of 'x's and 'o's.")
print("The string can contain any char.")

user_input = input("Enter your string: ")

count = 0

for x in user_input:
    
    if x == 'x' or x == 'X':
        count += 1

    elif x == 'o' or x == 'O':
        count -= 1

print(count == 0)
=======
print("Check to see if a string has the same amount of 'x's and 'o's.")
print("The string can contain any char.")

user_input = input("Enter your string: ")

count = user_input.count('x') + user_input.count('X')
count -= user_input.count('o') - user_input.count('O')

print(count == 0)
>>>>>>> 715fd0763b415a13fb28a483f258a5eadc1ec931
