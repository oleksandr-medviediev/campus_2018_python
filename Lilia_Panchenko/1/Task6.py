str = input('Please, input PIN to validate:\n')

is_pin_valid = True

len_str = len(str)
	
if (not (len_str == 4 or len_str == 6)):
	is_pin_valid = False
	 
if is_pin_valid:	 
	try:
		pin = int(str)
	
	except ValueError:
		is_pin_valid = False
	
print (is_pin_valid)
