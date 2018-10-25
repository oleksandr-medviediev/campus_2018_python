singles = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def say_number(number):

    """
    Takes number and spells it.



    """
    output = ""

    string = str(number)

    output += singles[int(string)]
    
    return output


print(say_number(9))