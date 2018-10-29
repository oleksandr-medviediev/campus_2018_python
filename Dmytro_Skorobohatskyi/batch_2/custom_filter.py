def custom_filter(predicate, collection):

    """ Function returns only those values of collection,
        which meet the condition of predicate.

    Args:
        predicate(function): function or lambda returned bool value or None
        collection(list): specified collection

    Returns:
        list: new list with values, which meet the predicate's condition.
        
    """
    
    if predicate == None:
        return collection
    
    filtered_collection = []

    for i, el in enumerate(collection):
        if predicate(el):
            filtered_collection.append(el)

    return filtered_collection
