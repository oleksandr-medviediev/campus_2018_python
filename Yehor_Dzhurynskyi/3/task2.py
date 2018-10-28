import math


def encode(in_string):
    """
    encodes string using square crypto method
        :param str in_string: text that should be encoded
        :return: encoded string
        :rtype: str
    """

    normalized_string = ''.join(ch for ch in in_string.lower() if ch.isalnum())

    width = math.ceil(math.sqrt(len(normalized_string)))
    height = math.ceil(len(normalized_string) / width)

    words = [normalized_string[i * width: i * width + width] for i in range(height)]
    encoded = ''.join([word[x] for x in range(width) for word in words if x < len(word)])

    return encoded


def decode(in_string):
    """
    decodes string using square crypto method
        :param str in_string: text that should be decoded
        :return: decoded string
        :rtype: str
    """

    width = math.ceil(math.sqrt(len(in_string)))
    height = math.ceil(len(in_string) / width)

    words = [in_string[i * height: i * height + height] for i in range(width)]
    decoded = ''.join([word[x] for x in range(height) for word in words if x < len(word)])

    return decoded
