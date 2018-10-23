print("ATM machines allow 4 or 6 digit PIN codes")
print("and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.")

user_input = input("Enter PIN: ")
user_input_len = len(user_input)
is_pin_valid = True

if user_input_len != 4 and user_input_len != 6:

    is_pin_valid = False

else:

    for x in user_input:

        if not x.isnumeric():

            is_pin_valid = False
            break

print(is_pin_valid)
