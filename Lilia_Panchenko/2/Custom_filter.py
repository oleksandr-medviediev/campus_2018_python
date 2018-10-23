def m_filter (func, sequence):
	
	"""
	m_filter (func, sequence)
	It's a custom filter fuction. Filter out all the elements of a sequence "sequence", for which the function 'function' returns True.

    Args:
        func (function): Function to use as filter.
        sequence (list): List to perform function at.

    Returns:
        list: list of elements where function(element) returned True
    """

	return_sequence = []

	for elem in sequence:
		if (func(elem)):
			return_sequence.append(elem)

	return return_sequence

print(m_filter.__doc__)
