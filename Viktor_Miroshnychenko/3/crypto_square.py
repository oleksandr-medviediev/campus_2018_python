def find_rect(number):
    """
    :param number: number representing s length of string that rect is search for
    :type number: int

    :return: list of width and height
    :rtype: list
    """

    width = 0
    height = 2
    while height - width > 1:
        width += 1
        height = number // width
        if number % width > 0:
            height += 1

    if height > width:
        height, width = width, height


    return [width, height]
    

def encode(string):
    """
    :param string: string to encode
    :type string: str

    """

    string = string.replace(" ","")
    print(string)
    string.lower()
    rect = find_rect(len(string))
    encoded_string = ""
    for count in range(rect[0]):
        i = count
        while i < len(string):
            encoded_string += string[i]
            i += rect[0]

    print(encoded_string)
    return encoded_string
        
        

def decode(string):
    """
    :param string: string to decode
    :type string: str

    :return: decoded string
    "rtype: str
    """
    string.replace(" ","")
    string.lower()
    rect = find_rect(len(string))
    last_row_len = len(string) - rect[0] * (rect[1] - 1)
    print(last_row_len)
    encoded_string = ""
    for count in range(rect[1]):
        i = count
        while i < len(string):
            encoded_string += string[i]
            i += rect[1]
            if last_row_len < i // rect[1]:
                i -= 1
            if len(encoded_string) == len(string):
                break;
    
    return encoded_string



#print(encode("param"))
#print(decode("paamr"))
#Some string to encode - decode with whitespaces
print(decode(encode("Some string to encode and decode with whitespaces")))
