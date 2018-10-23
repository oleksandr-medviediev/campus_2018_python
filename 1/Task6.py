str = input('Please, input PIN to validate:\n')

is_pin_valid = True

len_str = len(str)
	
if (not (len_str == 4 or len_str == 6) or not str.isnumeric()):
	is_pin_valid = False
	
print (is_pin_valid)
