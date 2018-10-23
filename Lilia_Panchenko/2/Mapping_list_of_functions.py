def map_functions(object, list_functions):
	
	"""
	map_functions(object, list_functions)
	It's a special map fuction. It perform given list of functions on object

    Args:
        object (any): Object to perform list of functions at
        list_functions (list): List of functions.

    Returns:
        list: result of performing functions on object. Each element of result list corresponds to result of performing of each function
    """
	result = []
	
	for i in list_functions:
		result.append(i(object))
		
	return result

print(map_functions.__doc__)
