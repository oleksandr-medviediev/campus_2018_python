def encode(endoding_string):
    
    """Takes string and encodes it using Run-length encoding. Returns encoded string."""

    output_string = ""
    current_char = ''
    current_count = 0

    for ch in endoding_string:

        if current_char != ch:

            if current_count != 0:

                output_string += str(current_count) + current_char

            current_char = ch
            current_count = 0

        current_count += 1
    
    if(current_count != 0):

        output_string += str(current_count) + current_char

    return output_string


def decode(decoding_string):
    
    """Takes string and decodes it using Run-length decoding. Returns decoded string."""

    output_string = ""
    current_count_str = ""

    for ch in decoding_string:

        if  str(ch).isdigit():
            
            current_count_str += ch
            continue
        
        for i in range(int(current_count_str)):

            output_string += ch
        current_count_str = ""

    return output_string


print(decode(encode("AAAAAAAAAASSSSSSSSSSVVVVVVVVVCCCCCCCXVVVVVVVV")))
