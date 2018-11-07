def spell_number(number):
    """Function convert number in word phrase.

    Args:
        number: type integer.

    Returns:
        Return string.

    """
    dict_number = {
        0: "zero",
        1: "one",
        2: "two",
        3: "tree",
        4: "for",
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
        40: "fourty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninty"
    }

    type_value = {
        1: "thousand",
        2: "million",
        3: "billion"
    }

    if number in dict_number:
        result = dict_number[number]
        return result

    digits = list(str(number))

    number_parties = []
    tmp_list = []

    for i in range(len(digits) - 1, -1, -1):
        tmp_list.insert(0, digits[i])
        if (len(tmp_list) == 3) and (i < (len(digits) - 1)):
            number_parties.insert(0, tmp_list)
            tmp_list = []

    if tmp_list:
        number_parties.insert(0, tmp_list)

    del(tmp_list)

    result = []
    count = 0

    for arr in number_parties:
        if count > 0:
            result.append(type_value[count])
            result.append("and")

        for i in range(len(arr)):
            if int(arr[i]) == 0:
                continue
            elif (i == 0) and (len(arr) == 3):
                result.append(dict_number[int(arr[i])])
                result.append("hundred")

                if (int(arr[i + 1]) == 0) and (int(arr[i + 2]) == 0):
                    break
                else:
                    result.append("and")
            elif ((i == 1) and (len(arr) == 3)) or (len(arr) == 2):
                string = arr[i] + arr[i + 1]
                if int(string) in dict_number:
                    result.append(dict_number[int(string)])
                else:
                    result.append(dict_number[int(arr[i]) * 10])
                    result.append(dict_number[int(arr[i + 1])])
                break
            else:
                if int(arr[i]) in dict_number:
                    result.append(dict_number[int(arr[i])])
        count += 1
    
    if result[len(result) - 1] == "and":
        result.pop()

    result_string = ' '.join(result)

    return result_string


if __name__ == '__main__':
    result = spell_number(245300)
    print(result)
