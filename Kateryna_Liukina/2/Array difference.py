def array_difference(ar1, ar2):
    """Finds the difference between two list
	Args:
        ar1(list): first collection
        ar2(list): second collection
    Returns:
        list: new list with values of first collection,
              excluding values from second.
			  
	"""
    return list(set(ar1)-set(ar2))


def array_difference2(ar1, ar2):
    """Finds the difference between two list
	Args:
        ar1(list): first collection
        ar2(list): second collection
    Returns:
        list: new list with values of first collection,
              excluding values from second.
			  
	"""
    return [i for i in ar1 if i not in ar2]

