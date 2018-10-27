print("Implement run-length encoding and decoding.")


def encode(arg):
    """
    Function encodes given string to run-length format

    :param str arg: string with letters
    :return: run-length encoded string
    :rtype: str 
    """

    count = 1
    previous_char = ''
    encoded_list = []

    for char in arg:

        if char != previous_char:

            if previous_char:

                encoded_entry = (count, previous_char)
                encoded_list.append(encoded_entry)

            count = 1
            previous_char = char

        else:

            count += 1

    encoded_entry = (count, previous_char)
    encoded_list.append(encoded_entry)

    encoded_string = str()

    for count, char in encoded_list:

        if count > 1:

            encoded_string += str(count) + char

        else:

            encoded_string += char

    return encoded_string


def decode(arg):
    """
    Function decodes given encoded string in run-length format

    :param str arg: encoded string
    :return: decoded string of letters
    :rtype: str 
    """

    decoded_string = str()
    char_count = ''
    prev_char = ''

    for char in arg:

        if char.isnumeric():

            char_count += char

        else:

            if prev_char.isnumeric():

                decoded_string += char * int(char_count)
                char_count = ''

            else:

                decoded_string += char

        prev_char = char

    return decoded_string

    

user_input = input("Enter string to encode and decode ")

encoded_user_input = encode(user_input)
decoded_user_input = decode(encoded_user_input)

print("Your ecoded string: ", encoded_user_input)
print("Your decoded string: ", decoded_user_input)
