from collections import OrderedDict


def Encode(data):
    """
    Caesar's cypher(Rotational cypher). More info https://en.wikipedia.org/wiki/Caesar_cipher .

    Args:
        data (str): string data.

    Returns:
        str, encoded data.
    """
    encoded_string = list()

    last_symbol = None
    counter = 0
    for i in data:
        if i == last_symbol:
            counter += 1
        else:
            encoded_string.append([counter + 1, last_symbol])
            counter = 0
            last_symbol = i
    encoded_string.append([counter + 1, last_symbol])
    return encoded_string[1:]


def Decode(data):
    """
    Caesar's cypher(Rotational cypher). More info https://en.wikipedia.org/wiki/Caesar_cipher .

    Args:
        data (str): string data.

    Returns:
        str, decoded data.
    """
    res = ""
    for entry in data:
        for i in range(0, entry[0]):
            res += entry[i]
    return res


to_code = "WWWwwwAAAwwWWWWWWWW"
print("Encoding string: " + to_code)
data = Encode(to_code)
print(data)
print(Decode(data))
