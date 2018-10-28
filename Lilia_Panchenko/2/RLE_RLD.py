def rle(str_to_encode):
	"""
	rle(str_to_encode)
	This function returns encoded with Run length encoding (RLE).

    Args:
        str_to_encode(str): string, which needs to be encoded

    Returns:
        str: encoded with RLE string
    """
	encoded = ''
	fmt = '{}{}'
	
	i = 1
	curr_char = str_to_encode[0]
	count_curr_char = 1
	
	while i < len(str_to_encode):
		if str_to_encode[i] == curr_char:
			count_curr_char += 1
		else:
			if count_curr_char > 1:
				encoded += fmt.format(count_curr_char, curr_char)
			else:
				encoded += curr_char
				
			curr_char = str_to_encode[i]
			count_curr_char = 1
			
		i+=1
	
	return encoded
	
def rld(str_to_decode):
	"""
	rld(str_to_decode)
	This function returns decoded string, which was encoded with Run length encoding (RLE).

    Args:
        str_to_decode(str): encoded string, which needs to be decoded

    Returns:
        str: decoded RLE string
    """
	decoded = ''
	
	count = 0
	
	i = 0
	while i < len(str_to_decode):
		
		c = str_to_decode[i]
		if c.isdigit():
			count = count * 10 + int(c)
		else:
			if count > 0:
				count = int(count)
			else:
				count = 1
				
			decoded += c * count
			count = 0
			
		i+= 1
	
	return decoded
