while True:

    in_string = input('Enter your string to test on "o" and "x" content ')
    in_string = in_string.lower()

    o_quantity = in_string.count('o')
    x_quantity = in_string.count('x')

    if o_quantity == x_quantity:

        print('True')

    else:

        print('False')
