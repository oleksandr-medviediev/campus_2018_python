"""
This script solves task 2.7 from Coding Campus 2018 Python course
(Run length encoding)
"""


def write_char_to_list(last_character, character_count):
    """
    Convenience function to form character and count pairs for RLE encode
    :param last_character: Character occurred on previous iteration
    :param character_count: Count of mentioned character
    :return: List to append to encode return string
    """

    return_list = []
    if character_count > 1:
        return_list += [str(character_count), last_character]
    else:
        return_list += last_character

    return return_list


def rle_encode(string):
    """
    Encodes string using Run-Length encoding
    :param string: Input raw string
    :return: RLE-encoded string
    """

    list_string = list(string)
    last_character = None
    character_count = 0
    return_list = []

    for index in range(len(list_string)):

        character = list_string[index]

        if last_character != character:

            if last_character is not None:
                return_list += write_char_to_list(last_character, character_count)

            last_character = character
            character_count = 1
        else:
            character_count += 1

        if index == (len(list_string) - 1):
            return_list += write_char_to_list(last_character, character_count)

    return ''.join(return_list)


def rle_decode(string):
    """
    Decodes string using Run-Length encoding
    :param string: Input encoded string
    :return: Raw decoded string
    """

    list_string = list(string)
    last_character = None
    is_last_character_number = False
    character_count = 0
    return_list = []
    number_buffer = []

    for character in list_string:

        if not character.isdigit() and is_last_character_number:

            count = int(''.join(number_buffer))
            return_list += [character for i in range(count)]

            number_buffer.clear()
            is_last_character_number = False

        if character.isdigit():

            number_buffer.append(character)
            is_last_character_number = True
        else:
            return_list += character

    return ''.join(return_list)


print("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB")
print(rle_encode("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"))
print(rle_decode("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"))
