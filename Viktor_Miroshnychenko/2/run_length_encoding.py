def encode(string):
    """
    :param string: = string to encode:
    :type string: = str
    
    :return:  = encoded string
    :rtype: = str
    """
    if string == "":
        return ""
    
    current_letter = string[0]
    length = 0
    ret_val = ""
    for char in string:
        if char == current_letter:
            length += 1
        else:
            ret_val += str(length)
            ret_val += current_letter
            length = 1
            current_letter = char
    ret_val += str(length)
    ret_val += current_letter

    return ret_val


def decode(string):
    """
    :param string: = string to decode:
    :type string: = str
    
    :return:  = decoded string
    :rtype: = str
    """
    if string == "":
        return ""

    string = list(string)
    ret_val = ""
    count = 1
    for char in string:
        if char.isdigit():
            count = int(char)
        else:
            ret_val += char * count
            count = 1

    return ret_val

    
print(encode("FHHGKKSSFEFELJNFELAAAAAAAAAAAAAAAa"))
print(decode("1F3AJ8G9HIOD7D8D5DGJ2DD"))
