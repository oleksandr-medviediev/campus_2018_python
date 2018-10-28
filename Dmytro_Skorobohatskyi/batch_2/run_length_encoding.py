def encode(string):

    """ Function encode string by run-length-encoding.

    Args:
        string(str): string to encode

    Returns:
        str: encoded string
        
    """
    
    if string == None or len(string) == 0:
        return ""
    
    result = []

    #symbol od end
    process_string = string + '^'
    
    current_char = process_string[0]
    counter = 0
    for i, el in enumerate(process_string):
        if current_char == el:
            counter += 1
        else:
            if counter != 1:
                result.append(counter)
                
            result.append(current_char)
            counter = 1
            current_char = el

    return result


def decode(string):

    """ Function decode string by run-length-encoding.

    Args:
        string(str): string to decode

    Returns:
        str: decoded string
        
    """
    
    result_list = []

    process_list = []
    process_list.extend(string)

    counter = 0
    i = 0
    while i < len(process_list):
        if process_list[i].isalpha() or process_list[i].isspace():
            result_list.append(process_list[i])
        elif process_list[i].isdigit():
            while process_list[i].isdigit():
                counter = counter * 10 + int(process_list[i])
                i += 1

            symbol = process_list[i]
            for j in range(counter):
                result_list.append(symbol)
                
            counter = 0

        i += 1

    decoded_string = "".join(result_list)

    return decoded_string
