print("Check to see if a string has the same amount of 'x's and 'o's.")
print("The string can contain any char.")

user_input = input("Enter your string: ")

x_count = 0
o_count = 0

for x in user_input:
    
    if x == 'x' or x == 'X':
        x_count += 1

    elif x == 'o' or x == 'O':
        o_count += 1

if x_count == o_count and x_count != 0 and o_count != 0:
    print("True")

else:
    print("False")
