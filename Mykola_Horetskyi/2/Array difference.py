def array_diff1(array1, array2):
    
    """
    Removes from array1 all elements present in array2
    
Args:
    array1 (list) list from which elements are removed
    array2 (list) list belonging to which is a criteria for removing
    

Returns:
    list that is array1 with all elements that also present in array2 removed
"""

    result = list(filter(lambda element: not element in array2, array1))

    return result


def array_diff2(array1, array2):
    """
Removes from array1 all elements present in array2
Args:
array1 (list) list from which elements are removed
array2 (list) list belonging to which is a criteria for removing

Returns:
list that is array1 with all elements that also present in array2 removed
"""

    result = []

    for element in array1:
        if not element in array2:
            result.append(element)
    
    return result
