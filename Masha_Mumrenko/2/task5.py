def custom_filter(function, to_apply):
    result = []
    for element in to_apply:
        if function(element):
            result.append(element)

    return result
