def is_armstrong(n):
	
	"""
	is_armstrong(n)
	This function determine if number is Armstrong number. 

    Args:
        n (int): number to check

    Returns:
        bool: True if n was Armstrong, False - otherwise
    """
	n_digits = {int(d) for d in str(n)}
	
	global len_list
	len_list = len(n_digits)
	
	n_digits_pow = list(map(lambda x: x**len_list, n_digits))
	to_compare = sum(n_digits_pow)
	
	return to_compare == n
