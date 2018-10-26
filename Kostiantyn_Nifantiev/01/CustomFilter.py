def custom_filter(predicate, array):
    """
        This filter directly accumulates result by applying 
        predicate to initial array
    """
    if not len(array): 
        
        print('Wrong input!') 
        return
    
    result = list()
    
    for item in array:
    
        if predicate(item): result.append(item)

    return result

print(custom_filter(lambda x: x < 10, [1, 2, 3, 5, 8, 13, 21]))
