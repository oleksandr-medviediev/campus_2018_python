def list_difference(list1, list2):
	
	"""
	list_difference(list1, list2)
	This function returns list which is result of list1 except list2 

    Args:
        list1 (list): List to exclude from
        list2 (list): List of elements to exclude

    Returns:
        list: result of excluding all elements of list2 from list1
    """
	result_list = list1
	
	for x in list2:
		result_list = list(filter(lambda elem: elem != x, result_list))
		
	return result_list
