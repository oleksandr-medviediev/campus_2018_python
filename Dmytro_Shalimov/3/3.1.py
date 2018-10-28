print("3.1 Spell number")


MAX_LEN = 12
NUMBERS_IN_WORDS = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",
 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
 16: "sixteen", 17: "seventeen", 18: "eightteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "fourty",
 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}

HUNDRED_WORD = "hundred"
THOUSAND_WORD = "thousand"
MILLION_WORD = "million"
BILLION_WORD = "billion"
AND_WORD = "and"

BILLION = 1000000000
MILLION = 1000000
THOUSAND = 1000


def number_input():
    """
    Promts user to enter number until input is correct

    :return: user input in string
    :rtype: str
    """

    while True:

        user_input = input("Enter number from 0 to 999.999.999.999: ")

        if len(user_input) in range(1, MAX_LEN + 1) and user_input.isdigit():
            return user_input

        else:
            print("Invalid input, try again")


def process_number(number):
    """
    Processes numbers from 0 to 999 and writes its word equivalent in output string

    :param int number: number in int
    :return: string with number in words equivalent
    :rtype: str
    """

    current_number = number
    output = ''

    while True:

        if current_number >= 100:

            output += f"{NUMBERS_IN_WORDS.get(current_number // 100)} {HUNDRED_WORD} "

            if current_number % 100 > 0:

                output += f"{AND_WORD} "
                current_number %= 100

            else:
                break

        elif current_number >= 10:

            if current_number <= 20:

                output += f"{NUMBERS_IN_WORDS.get(current_number)} "
                break

            else:

                output += f"{NUMBERS_IN_WORDS.get(current_number - current_number % 10)} "
                current_number %= 10

        else:

            output += f"{NUMBERS_IN_WORDS.get(current_number)} "
            break

    return output


user_number = number_input()

current_number_len = len(user_number)
current_number = int(user_number)

output = ''

while True:

    if current_number_len >= MAX_LEN - 2:

        number_to_process = current_number // BILLION
        current_number_len = 9

        output += process_number(number_to_process)
        output += f"{BILLION_WORD} "

        current_number %= number_to_process * BILLION

        if current_number == 0:
            break

    elif current_number_len >= MAX_LEN - 5:

        number_to_process = current_number // MILLION
        current_number_len = 6

        if number_to_process == 0:
            continue

        output += process_number(number_to_process)
        output += f"{MILLION_WORD} "

        current_number %= number_to_process * MILLION

        if current_number == 0:
            break

    elif current_number_len >= MAX_LEN - 8:

        number_to_process = current_number // THOUSAND
        current_number_len = 3

        if number_to_process == 0:
            continue

        output += process_number(number_to_process)
        output += f"{THOUSAND_WORD} "

        current_number %= number_to_process * THOUSAND

        if current_number == 0:
            break

    else:

        if current_number <= 100 and len(output) > 0:
            output += f"{AND_WORD} "

        output += process_number(current_number)
        break

print(output)
