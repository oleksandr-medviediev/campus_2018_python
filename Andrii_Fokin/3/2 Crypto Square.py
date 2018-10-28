from math import sqrt


def encode(sentence_incoming):
    """Hash message acording to square code"""
    sentence_normalized = ''.join([ch for ch in sentence_incoming if ch.isalpha()]).casefold()
    number_of_coloms = int(sqrt(len(sentence_normalized))) + 1
    sentence_squared = list()

    for i in range(number_of_coloms):
        start =  int(number_of_coloms * i)
        end = int(min(start + number_of_coloms, len(sentence_normalized)))
        if start < end:
            sentence_squared.append(sentence_normalized[start:end])

    result = ''.join([''.join(res) for res in zip(*sentence_squared)])
    return result


def decode(sentence_hashed):
    """Decode message which was hashed according to square code"""
    number_of_coloms = int(sqrt(len(sentence_hashed)))
    sentence_squared = list()

    for i in range(number_of_coloms):
        start =  int(number_of_coloms * i)
        end = int(min(start + number_of_coloms, len(sentence_hashed)))
        if start < end:
            sentence_squared.append(sentence_hashed[start:end])

    result = ''.join([''.join(res) for res in zip(*sentence_squared)])
    return result




print(encode("If man was meant to stay on the ground, god would have given us roots."))
print(decode("imtgdvsfearwermayoogoanouuiontnnlvtwttddesaohghnsseoau"))