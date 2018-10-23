def is_time_valid(time_str):
	time_strings = time_str.split(':')
	len_time_strings = len(time_strings)

	is_valid = True

	if len_time_strings != 2 or len(input_str) > 5:
		is_valid = False

	if is_valid:	
		hours = time_strings[0]
		minutes = time_strings[1]

		if not hours.isnumeric() or not minutes.isnumeric():
			is_valid = False
		
	if is_valid:

		hours = int(hours)
		minutes = int(minutes)

		if (hours > 23 or hours < 0) or (minutes > 59 or minutes < 0):
			is_valid = False

	return is_valid, hours, minutes

input_str = input('Please, input time to convert:\n')
		
is_valid, h, m = is_time_valid(input_str)

if is_valid:

	result = ''
	format_mid = '12:{0:d} {:s}'
	format_default = '{0:d}:{0:d} {:s}'

	if h < 12 and h != 0:
		result = format_default.format(h, m, 'am')
		
	elif (h == 0):
		result = format_mid.format(m, 'am')
	elif (h == 12):
		result = format_mid.format(m, 'pm')		
	else:
		result = format_default.format(h - 12, m, 'pm')

	print(result)
		
else:
	print ('not a valid time')
