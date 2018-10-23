def shift_char(char):
	if char.islower():
		ord_start = ord('a')
	else:
		ord_start = ord('A')

	new_index = ord(char) - ord_start + shift - 1
	new_index = (new_index % 26) + ord_start
	char = chr(new_index)
	return char


input_shift = input('Please, input shift value to cipher:\n')
is_shift_valid = input_shift.isnumeric()

if (is_shift_valid):

	global shift
	shift = int(input_shift)

	input_str = input('Please, input some string to encrypt:\n')

	encryption = ''
	
	for i in range(len(input_str)):
		letter = input_str[i]

		if letter.isalpha():
			letter = shift_char(letter)
			
		encryption += letter
	
	print(encryption)

else:
	print('Non-integer as shift value!')