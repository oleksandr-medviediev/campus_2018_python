def rle_encode(original_string):

    """
    Encodes string using run-length encoding

Args:
    original_string (str) string to encode

Returns:
    (str) encoded string
    """

    encoded_string = ''
    
    current_character = ''
    
    character_count = 0

    for character in original_string:
        if character == current_character:
            character_count += 1
        else:
            if  character_count > 1:
                encoded_string += str(character_count) + current_character
            elif character_count ==1:
                 encoded_string += current_character

            current_character = character
            character_count = 1

    if  character_count > 1:
        encoded_string += str(character_count) + current_character
    elif character_count ==1:
        encoded_string += current_character

    return encoded_string


def rle_decode(encoded_string):
    """
    Decodes string using run-length decoding

Args:
    encoded_string (str) string to decode

Returns:
    (str) decoded string
    """

    decoded_string = ''
    current_count_string = ''

    for character in encoded_string:
        if character.isdigit():
            current_count_string += character
        elif current_count_string:
            decoded_string += int(current_count_string) * character
            current_count_string = ''
        else:
            decoded_string += character

    return decoded_string
    

    
    
