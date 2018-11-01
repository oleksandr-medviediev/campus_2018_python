def find_odd1(array):
    """Returns the first int element that appears odd number of times in list

Args:
    array (list) array that is searched for mentiond element

Returns:
    first int element that appears odd number of times in array
    or None if there is no such element
    """
    
    for element in array:
        if type(element) is int and array.count(element) % 2 != 0:
            return element

    return None


def find_odd2(array):

    filtered_elements = list(filter(lambda element: type(element) is int and array.count(element) % 2 != 0, array))

    if filtered_elements:
        return filtered_elements[0]

    return None

def find_odd3(array):

    oddity_check = list(map(lambda element: type(element) is int and array.count(element) % 2 != 0, array))

    for i in range(len(oddity_check)):
        if oddity_check[i]:
            return array[i]

    return None
