input_str = input('Please, input time to validate:\n')

time_strings = input_str.split(':')
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
		
print (is_valid)
