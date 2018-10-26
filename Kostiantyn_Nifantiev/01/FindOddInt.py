numeric_string = input('Enter string with numbers to check. Use "," as delimiter: ')
numeric_tokens = numeric_string.split(',')
numbers_list = list()

for token in numeric_tokens:

    if token.isnumeric(): numbers_list.append(int(token))

print(numbers_list)

def first(num_list):
    """
        Crude, direct count
    """
    result = 'There is no odd-times appearing int!'

    for i in range(len(num_list)):
    
        entries = num_list
        
        for num in num_list:
        
            if num_list[i] == num: entries += 1
        
        if entries % 2: 
            
            result = num_list[i]
            break

    return result

def second(num_list):
    """
        More elegant xor-based method
    """
    accumulator = int()

    for num in num_list: accumulator ^= num
    
    if num_list.count(0) % 2: return 0

    elif accumulator: return accumulator

    else: return('There is no odd-times appearing int!')

def third(num_list):
    """
        More pythonic (i hope) version
    """
    result = 'There is no odd-times appearing int!'

    for num in num_list:

        if num_list.count(num) % 2:

            result = num
            break

    return result

print(first(numbers_list))
print(second(numbers_list))
print(third(numbers_list))
