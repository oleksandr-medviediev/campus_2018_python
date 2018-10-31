def custom_filter(func, container):
    """Find every item in given container that func of item returns true
	
	Args:
        func(function): function or lambda returned bool value or None
        container(list): specified collection
    Returns:
        list: new list with values, which meet the func's condition.
	"""
    return [i for i in container if func(i)]
