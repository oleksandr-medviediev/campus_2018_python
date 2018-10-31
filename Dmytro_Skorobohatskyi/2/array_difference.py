#approach_1
def array_difference(arr_1, arr_2):

    """ Function returns first collection without elements
        which contain in second and do not modify both ones.
        Realized with using of set's possibilities.

    Args:
        arr_1(list): first collection
        arr_2(list): second collection

    Returns:
        list: new list with values of first collection,
              excluding values from second.
        
    """
    
    set_1 = set(arr_1)
    set_2 = set(arr_2)

    result_array = set_1 - set_2

    return result_array


#approach_2
def array_difference_2(arr_1, arr_2):

    """ Function returns first collection without elements
        which contain in second and do not modify both ones.

    Args:
        arr_1(list): first collection
        arr_2(list): second collection

    Returns:
        list: new list with values of first collection,
              excluding values from second.
        
    """
    
    result = arr_1.copy()
    
    for i, el in enumerate(arr_2):
        while el in result:
            result.remove(el)

    return result
