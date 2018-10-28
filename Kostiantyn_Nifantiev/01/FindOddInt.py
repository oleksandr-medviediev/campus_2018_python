numeric_string = input('Enter string with numbers to check. Use "," as delimiter: ')
numeric_tokens = numeric_string.split(',')

numbers_list = [int(token) for token in numeric_tokens if token.isnumeric()]
print(numbers_list)


def first(num_list):
    """
        Crude, direct count
    """
    result = 'There is no odd-times appearing int!'

    for i in range(len(num_list)):
    
        entries = num_list.count(num_list[i])
        
        if entries % 2: 
            
            result = num_list[i]
            break

    return result


def second(num_list):
    """
        More elegant xor-based method
    """
    accumulator = 0

    for num in num_list:

        accumulator ^= num
    
    if num_list.count(0) % 2:

        return 0

    return accumulator or 'There is no odd-times appearing int!'


def third(num_list):
    """
        More pythonic (i hope) version
    """
    result = None

    for num in num_list:

        if num_list.count(num) % 2:

            result = num
            break

    return result or 'There is no odd-times appearing int!'


print(first(numbers_list))
print(second(numbers_list))
print(third(numbers_list))
