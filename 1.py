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
