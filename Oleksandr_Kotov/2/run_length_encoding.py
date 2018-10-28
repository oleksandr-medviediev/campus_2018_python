def encode(string):
    """encode the sequence of characters to RLE"""

    output = ""

    current_char = ''
    occurencies = 0

    for char in string:

        if current_char == char:
            occurencies +=1
            
        else:
            if occurencies > 1:
                output += str(occurencies)

            output += current_char

            current_char = char
            occurencies = 1

    if occurencies > 1:
        output += str(occurencies)

    output += current_char

    return output




def decode(string):
    """decode the sequence of characters from RLE"""

    output = ""
    number = ""

    for char in string:
        if char.isnumeric():
            number += char

        else:
            if number == "":
                output += char

            else:
                for i in range(int(number)):
                    output += char

                number = ""


    return output




print(encode("WWWBBBBA"))
print(decode("2AB3CD4E"))