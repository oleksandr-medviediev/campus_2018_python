from math import sqrt


def encode(sentence):
    """encodes passed sentence

    Arguments:
        sentence {str} -- sentence to encode

    Returns:
        str -- encoded sentence
    """
    normalized_sentence = ''.join(
        [ch for ch in sentence if ch.isalpha()]).casefold()

    columns = int(sqrt(len(normalized_sentence))) + 1
    squared_sentence = list()

    for i in range(columns):
        start = int(columns * i)
        end = int(min(start + columns, len(normalized_sentence)))
        if start < end:
            squared_sentence.append(normalized_sentence[start:end])

    result = ''.join([''.join(res) for res in zip(*squared_sentence)])
    return result


def decode(sentence):
    """encodes passed sentence
    
    Arguments:
        sentence {str} -- sentence to decode
    
    Returns:
        str -- decoded sentence
    """

    columns = int(sqrt(len(sentence)))
    squared_sentence = list()

    for i in range(columns):
        start = int(columns * i)
        end = int(min(start + columns, len(sentence)))
        if start < end:
            squared_sentence.append(sentence[start:end])

    result = ''.join([''.join(res) for res in zip(*squared_sentence)])
    return result


print(encode("If man was meant to stay on the ground, god would have given us roots."))
print(decode("imtgdvsfearwermayoogoanouuiontnnlvtwttddesaohghnsseoau"))
