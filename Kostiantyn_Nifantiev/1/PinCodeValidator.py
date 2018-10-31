pin_code_to_validate = input('Enter your pin, please')

if len(pin_code_to_validate) == 4 or len(pin_code_to_validate) == 6:

    if pin_code_to_validate.isdecimal():

        print('True')

    else:

        print('False')

else:

    print('False')
