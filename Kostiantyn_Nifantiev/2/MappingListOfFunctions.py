def map_list_of_functions(iterable, functions_list):
    """
        Don't pass empty sequence! 
    """
    if not len(iterable): 
    
        print('Wrong input!')
        return None
    
    result = []

    for item in iterable:

        processed_item = list()

        for func in functions_list:

            processed_item.append(func(item))

        result.append(processed_item)

    return result


first = lambda x: x + x
second = lambda x: x * x

print(map_list_of_functions([1, 2, 3, 4, 5], [first, second]))
