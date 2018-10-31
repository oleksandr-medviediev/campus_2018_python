def custom_map(function, *collection):

    """ Function aplly function to collection(s) and
        returns list of result values. Amount of function's params
        need to corresponding with amount of collections' amount.

    Args:
        function: function or lambda
        collection(tuple): tuple of collections

    Returns:
        list: new list with values
        
    """
    
    result = []

    collection_tuple = tuple(zip(*collection))

    for i, el in enumerate(collection[0]):
        cur_params = collection_tuple[i]
        result.append(function(*cur_params))

    return result
