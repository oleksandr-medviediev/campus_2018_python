import re


def sqrt_int(value):
	"""
	calculates floor integer value, closest to square root to value
	: param : value (int)

	: return : square root of value
	: rtype: int
	"""
	min_diff = value
	root = 1

	left = 0
	right = value

	while right - left > 1:

		mid = (right + left) // 2

		diff = abs(value - mid*mid)
		if diff < min_diff:
			root = mid
			min_diff = diff

		if value > mid * mid:
			left = mid
		else:
			right = mid

	return root


def normalize_str(input_str):

	input_str = input_str.casefold()
	normalized = re.sub(r'\W+', '', input_str)
	
	return normalized


def calculate_rows_cols(input_str):
	
	len_input = len(input_str)

	cols = rows = sqrt_int(len_input)

	if len_input > cols * rows:
		cols += 1

	return rows, cols


def encrypt(input_str):
	"""
	:param : input_str :  string to encrypt

	: return : encrypted string
	: rtype : str
	"""
	rectangle = []
	start = 0
	len_input = len(input_str)
	rows, cols = calculate_rows_cols(input_str)

	while len_input > 0:

		stop = start + min(cols, len_input)
		rectangle.append(input_str[start:stop])

		start += cols
		len_input -= cols

	last_row = rectangle[rows-1]

	rectangle[rows-1] = last_row + ' ' * (cols - len(last_row)) 
	rectangle = [list(rectangle[i]) for i in range(len(rectangle))]

	encrypted = [''.join(s) for s in zip (*rectangle)]
	encrypted = [s.replace(' ', '') for s in encrypted]

	encrypted_str = ''.join(encrypted)

	return encrypted_str


def decrypt(rows, cols, input_str):
	"""
	:param : input_str :  string to decrypt

	: return : decrypted string
	: rtype : str
	"""

	rectangle = []
	start = 0
	len_input = len(input_str)

	cols, rows = calculate_rows_cols(input_str)

	unfull_rows = rows - len_input // rows
	full_rows = rows - unfull_rows

	for i in range(full_rows):

		stop = start + cols
		rectangle.append(input_str[start:stop])

		start += cols
		len_input -= cols

	for i in range(unfull_rows):
		stop = start + cols - 1
		rectangle.append(input_str[start:stop] + ' ')

		start += cols - 1
		len_input -= cols - 1

	rectangle = [list(rectangle[i]) for i in range(len(rectangle))]

	decrypted = [''.join(s) for s in zip (*rectangle)]
	decrypted = [s.replace(' ', '') for s in decrypted]

	decrypted_str = ''.join(decrypted)

	return decrypted_str


input_str = input('Enter string to encrypt:\n')

normal_input = normalize_str(input_str)

encrypted_str = encrypt(rows, cols, normal_input)
print('Encryption : ', encrypted_str)

decrypted_str = decrypt(rows, cols, encrypted_str)
print('Decryption : ', decrypted_str)
