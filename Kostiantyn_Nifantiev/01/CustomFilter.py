def custom_filter(predicate, array):
    """
        This filter directly accumulates result by applying 
        predicate to initial array
    """
    if not len(array): 
        
        print('Wrong input!') 
        return None
    
    result = [item for item in array if predicate(item)]

    return result


def my_predicate(x):

        return bool(x < 10)


list_to_filter = [11, 1, 2, 3, 5, 8, 13, 21]
print(custom_filter(my_predicate, list_to_filter))
