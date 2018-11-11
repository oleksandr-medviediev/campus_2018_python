def encode(word):
    """ Function performs run length encoding

        Args:
            word(str): string to encode

        Returns:
            str: encoded string.
    """
    encoded = []
    current_run_letter = word[0]
    occurrence_counter = 1
    trailing_letter = '_'  # for proper encoding of last run
    for letter in word[1:] + trailing_letter:
        if letter == current_run_letter:
            occurrence_counter += 1
        else:
            encoded_run = (str(occurrence_counter) if occurrence_counter > 1 else '') + current_run_letter
            encoded.append(encoded_run)
            current_run_letter = letter
            occurrence_counter = 1

    encoded_word = ''.join(encoded)
    return encoded_word


def decode(encoded_word):
    """ Function performs run length decoding

        Args:
            encoded_word(str): encoded string
        Returns:
            str: decoded string
    """
    decoded = []
    for i, letter in enumerate(encoded_word):
        if letter.isdigit():
            decoded.append(int(letter) * encoded_word[i + 1])
        elif not encoded_word[i - 1].isdigit():
            decoded.append(letter)

    decoded_word = ''.join(decoded)
    return decoded_word


encoded = encode('AAAAABBBC')
print(encoded)
print(decode(encoded))
