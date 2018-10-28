def encode(instring):
    """
        Runlength encoder
    """
    if not len(instring):

        print("Empty input!")
        return None
    
    result = str()
    last_item = instring[0]
    count = 0

    for item in instring:

        if item != last_item:
            
            result += str(count)
            result += str(last_item)
            count = 1
            last_item = item

        else:

            count += 1

    else:

        result += str(count)
        result += str(last_item)
    
    return result


def decode(data):
    """
        Runlength decoder
    """
    if data is None:

        print("Invalid incoming data!")
        return None

    result = ""
    
    number_accumulator = ""

    for character in data:

        if character.isdecimal(): 
            
            number_accumulator += character

        else: 
            
            result += character * int(number_accumulator)
            number_accumulator = ""

    return result


val_to_encode = input('Enter your string to encode. It should contain only characters and spaces: \n')
print(val_to_encode)

encoded = encode(val_to_encode)

print(encoded)
print(decode(encoded))

