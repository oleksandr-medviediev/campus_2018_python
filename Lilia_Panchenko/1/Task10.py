import string 

input_shift = input('Please, input shift value to cipher:\n')
input_str = input('Please, input some string to encrypt:\n')

try:
	shift = int(input_shift)
	is_shift_valid = True

except ValueError:
	is_shift_valid = False
	print('non-integer as shift value!')

if (is_shift_valid):
	encryption = ''
	
	for i in range(len(input_str)):
		letter = input_str[i]
		if (letter in list(string.ascii_letters)):
			letter_index = ord(letter)
			if (letter_index >= 97):
				ord_start = ord('a')
			else:
				ord_start = ord('A')
			letter_index += shift - ord_start
			letter_index = ((letter_index - 1)% 26) + ord_start
			letter = str(chr(letter_index))
		encryption += letter
	
	print(encryption)