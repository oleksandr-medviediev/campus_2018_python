def custom_map(function, *collection):

    result = []

    collection_tuple = tuple(zip(*collection))

    for i, el in enumerate(collection[0]):
        cur_params = collection_tuple[i]
        result.append(function(*cur_params))

    return result
