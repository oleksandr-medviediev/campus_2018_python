def odd_int1(list1):
	"""
	odd_int1(list1)
	This function returns value, which was in list exactly odd times. 

    Args:
        list1 (list): List to look for a value

    Returns:
        int: integer value which was in list exactly odd times.
    """
	count_elements = {i: list1.count(i) for i in list1}
	
	for i in count_elements:
		if count_elements[i] % 2 == 0:
			return i
			

def odd_int2(list1):
	"""
	odd_int2(list1)
	This function returns value, which was in list exactly odd times. 

    Args:
        list1 (list): List to look for a value

    Returns:
        value (int): integer value which was in list exactly odd times.
    """
	
	while len(list1) > 0:
		start_len = len(list1)
		curr_value = list1[0]
		
		list1 = list(filter(lambda elem: elem != curr_value, list1))
		
		if (start_len - len(list1)) % 2 == 0:
			return curr_value
			
			
def odd_int3(list1):
	"""
	odd_int3(list1)
	This function returns value, which was in list exactly odd times. 

    Args:
        list1 (list): List to look for a value

    Returns:
        value (int): integer value which was in list exactly odd times.
    """
	
	while len(list1) > 0:
		
		curr_value = list1[0]
		count_curr_value = 1
		list1.remove(curr_value)
		
		for x in list1:
			if x == curr_value:
				list1.remove(curr_value)
				count_curr_value += 1
				
		if count_curr_value % 2 == 0:
			return curr_value


print(odd_int1.__doc__)
print(odd_int2.__doc__)
print(odd_int3.__doc__)
