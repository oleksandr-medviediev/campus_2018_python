def m_map (func, sequence):
	
	"""
	m_map(func, sequence)
	It's a custom map fuction. It perform given function on each element of sequence

    Args:
        func (function): Function to perform.
        sequence (list): List to perform function at.

    Returns:
        list: result of performing function on argument list. Each element of result list corresponds to each element of argument list
    """

	return_sequence = []

	for elem in sequence:
		return_sequence.append(func(elem))

	return return_sequence

print(m_map.__doc__)