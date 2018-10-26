incoming_string = input('Enter your string to test it for isogramity: ')
incoming_string.lower()

if len(incoming_string) < 1:

    print("Nothing to deal with!")

elif not incoming_string.isalpha():

    print("Not an alphabetic string!")

else:

    tokens = incoming_string.split(' |-')
    prepared_string = ''.join(tokens)

    for letter in prepared_string:

        if prepared_string.count(letter) > 1:

            print("False")
            break

    else:

        print("True")
