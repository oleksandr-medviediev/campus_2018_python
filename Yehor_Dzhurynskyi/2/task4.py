def map_functions(subject, *args):

    results = [func(subject) for func in args]

    return results
