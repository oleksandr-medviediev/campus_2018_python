def say_hundred(number):
    """
    Spells non-negative number less than thousand in English.

Args:
    number(int) non-negative integer less than thousand

Returns:
    (str) string with spelling of the number or None
    """

    if number > 999:
        return None

    small_numbers = ( "zero", "one", "two", "three", "four", "five",
                  "six", "seven", "eight", "nine", "ten",
                  "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                  "sixteen", "seventeen", "eighteen", "nineteen")
      
    tens_numbers = ("", "", "twenty", "thirty", "forty", "fifty",
                    "sixty", "Sseventy", "eighty", "ninety")

    result = []
    
    ones = number % 10
    tens = (number % 100 - ones) // 10
    hundreds = (number % 1000 - 10 * tens - ones) // 100

    if hundreds > 0:
        result.append(small_numbers[hundreds])
        result.append("hundred")

    if tens > 1:
        result.append(tens_numbers[tens])
        
    if tens == 1:
        result.append(small_numbers[10 * tens + ones])
    elif ones > 0:
        result.append(small_numbers[ones])

    return " ".join(result)
    

def say_number(number):
    """
    Spells non-negative number less than trillion in English.

Args:
    number(int) non-negative integer less than trillion

Returns:
    (str) string with spelling of the number or None
    """

    if number > 999999999999:
        return None

    large_numbers = ("", "thousand", "million", "billion")

    result = []
    hundreds_list = []
    
    while number > 0:
        hundreds_list.append(number % 1000)
        number //= 1000

    hundreds_list.reverse()

    thousand_exponent = len(hundreds_list)

    for i in range(thousand_exponent):
        result.append(say_hundred(hundreds_list[i]))
        
        if i != thousand_exponent - 1:
            result.append(large_numbers[thousand_exponent - i - 1])

    return " ".join(result)
