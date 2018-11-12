input_number = input("enter a number to spell \n")


def speller(number):
    """this function spells the passed number

    
    Arguments:
        number {int} -- a number that needs to be spelled
    
    Returns:
        str -- spelled number
    """

    spelled_number = ""

    temp_number = list(number)

    spellings_of_numbers = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "hundred",
        1000: "thousand",
        1000000: "million",
        1000000000: "billion"
    }

    while True:
        if temp_number[0] == "0" and len(temp_number) != 1:
            del temp_number[0]
        else:
            break

    if len(temp_number) == 1:
        return spellings_of_numbers.get(int(temp_number[0]))

    current_number = int(temp_number[-2] + temp_number[-1])

    if current_number in spellings_of_numbers:
        if len(temp_number) > 2:
            spelled_number += " and " + \
                spellings_of_numbers.get(current_number)
        else:
            spelled_number += spellings_of_numbers.get(current_number)
            return spelled_number
    else:
        if len(temp_number) > 2:
            spelled_number += " and " + \
                spellings_of_numbers.get(int(temp_number[-2] + "0"))
            spelled_number += " " + \
                spellings_of_numbers.get(int(temp_number[-1]))
        else:
            spelled_number += spellings_of_numbers.get(
                int(temp_number[-2] + "0"))
            spelled_number += " " + \
                spellings_of_numbers.get(int(temp_number[-1]))
            return spelled_number

    if spelled_number == " and zero":
        if temp_number[-3] != '0':
            spelled_number = spellings_of_numbers.get(
                int(temp_number[-3])) + " hundred"
        else:
            spelled_number = ""
    else:
        spelled_number = spellings_of_numbers.get(
            int(temp_number[-3])) + " hundred" + spelled_number

    if len(temp_number) == 3:
        return spelled_number

    if len(temp_number) < 7:
        recursive_number = ''.join(temp_number[-len(temp_number):-3])
        if speller(recursive_number) != "zero":
            spelled_number = speller(recursive_number) + \
               " thousand " + spelled_number
        return spelled_number

    if len(temp_number) < 10:
        recursive_number = ''.join(temp_number[-6:-3])
        if speller(recursive_number) != "zero":
            spelled_number = speller(recursive_number) + \
                " thousand " + spelled_number

        recursive_number = ''.join(temp_number[-len(temp_number):-6])
        if speller(recursive_number) != "zero":
            spelled_number = speller(recursive_number) + \
                " million " + spelled_number
        return spelled_number

    if len(temp_number) < 13:
        recursive_number = ''.join(temp_number[-6:-3])
        if speller(recursive_number) != "zero":
            spelled_number = speller(recursive_number) + \
                " thousand " + spelled_number

        recursive_number = ''.join(temp_number[-9:-6])
        if speller(recursive_number) != "zero":
            spelled_number = speller(recursive_number) + \
                " million " + spelled_number

        recursive_number = ''.join(temp_number[-12:-9])
        if speller(recursive_number) != "zero":
            spelled_number = speller(recursive_number) + \
                " billion " + spelled_number
        return spelled_number


if input_number.isdigit() and int(input_number) <= 999999999999:
    output = speller(input_number)
else:
    output = "invalid input"

print(output)
