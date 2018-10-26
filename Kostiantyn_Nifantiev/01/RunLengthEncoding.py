def encode(iterable):
    """
        Runlength encoder
    """
    if not len(iterable): return "Empty input!"

    if not iterable.isalpha(): return "Non-character string! Remove all numbes and special symbols, please!"
    
    result = str()
    lastItem = iterable[0]
    count = 0

    for item in iterable:

        if item != lastItem: 
            
            result += str(count)
            result += str(lastItem)
            count = 1
            lastItem = item

        else:

            count += 1

    else:

        result += str(count)
        result += str(lastItem)
    
    return result

def decode(data):
    """
        Runlength decoder
    """
    result = str()
    
    number_accumulator = str()

    for character in data:

        if character.isdecimal(): 
            
            number_accumulator += character

        else: 
            
            result += character * int(number_accumulator)
            number_accumulator = str()

    return result

val_to_encode = input('Enter your string to encode. It should contain only characters and spaces: \n')
print(val_to_encode)
encoded = encode(val_to_encode)
print(encoded)
print(decode(encoded))

