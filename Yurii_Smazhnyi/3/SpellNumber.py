small_numbers = ( "Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                  "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                  "Eighteen", "Nineteen")
      
tens = ("", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety")
      
scale_numbers = ("", "Thousand", "Million", "Billion")

def parse_hundred(string):

    """
    Takes string up to 3 digits and returns spelling of it.

    @param string: string for parsing
    @returns: spelled number

    """

    str_len = len(string)

    if not str_len:
        
        return small_numbers[0]

    if str_len == 1:

        return small_numbers[int(string)]

    else:

        number = int(string)

        if number < 20:

            return small_numbers[number]

        hundred = ""
        ten = ""
        units = ""

        if str_len == 3:

            hundred = small_numbers[int(string[-3])] + " hundreds"

        ten = tens[int(string[-2])]

        units_index = int(string[-1])

        if units_index != 0:

            units = small_numbers[units_index]

    return hundred + " " + ten + " " + units


def say_number(number):

    """
    Takes number and spells it.

    @param number: number for spelling
    @returns: string with spelling of number
    """

    output = ""
    string = str(number)
    start_pos = len(string) - 1
    hundred_list = [string[::-1][i:i+3] for i in range(0, len(string), 3)]
    hundred_list = hundred_list[::-1]

    for i in range(len(hundred_list)):

        output += parse_hundred(hundred_list[i][::-1])
        output += " "
        output += scale_numbers[len(hundred_list) - 1 - i] + " "

    return output



print(say_number(999999999999))