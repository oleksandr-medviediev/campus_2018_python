def custom_filter(predicate, collection):

    if predicate == None:
        return collection
    
    filtered_collection = []

    for i, el in enumerate(collection):
        if predicate(el):
            filtered_collection.append(el)

    return filtered_collection
