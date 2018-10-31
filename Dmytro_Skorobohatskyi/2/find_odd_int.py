#approach 1
def find_odd_amount_int_1(numbers):

    """ Function returns number which appears in collection odd times.

    Args:
        numbers(list): list of numbers

    Returns:
        number(int): number which appears in numbers odd times
        
    """
    
    result = 0

    for i, el in enumerate(numbers):
        counter = numbers.count(el)
        if counter % 2 == 1:
            result = el
            break

    return result


#approach 2
def find_odd_amount_int_2(numbers):

    """ Function returns number which appears in collection odd times.

    Args:
        numbers(list): list of numbers

    Returns:
        number(int): number which appears in numbers odd times
        
    """
    
    numbers_counter = {}

    for i, el in enumerate(numbers):
        numbers_counter[el] = numbers_counter.get(el, 0) + 1

    result = 0
    
    for key in numbers_counter:
        if numbers_counter[key] % 2 == 1:
            result = key
            break

    return result


#approach 3
def find_odd_amount_int_3(numbers):

    """ Function returns number which appears in collection odd times.

    Args:
        numbers(list): list of numbers

    Returns:
        number(int): number which appears in numbers odd times
        
    """
    
    process_list = numbers.copy()
    stack = []

    first_elem_index = 0
    while len(process_list) != 0:
        value = process_list[first_elem_index]
        if value in stack:
            stack.remove(value)
        else:
            stack.append(value)

        process_list.remove(value)

    number = stack[0]

    return number
