print("Check to see if a string has the same amount of 'x's and 'o's.")
print("The string can contain any char.")

user_input = input("Enter your string: ")

count = user_input.count('x') + user_input.count('X')
count -= user_input.count('o') - user_input.count('O')

print(count == 0)
