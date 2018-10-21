str = input('Please, input time to validate:\n')

time_strings = str.split(':')
len_time_strings = len(time_strings)

should_validate_next = True

if (len_time_strings != 2):
	should_validate_next = False
	
next_part_index = 0
if (should_validate_next):
	try:
		hours = int(time_strings[next_part_index])
		next_part_index += 1 
		
		if (hours >= 24 or hours < 0):
			should_validate_next = False
			
	except ValueError:
		should_validate_next = False
	
if (should_validate_next):
	try:
		minutes = int(time_strings[next_part_index])
		
		if (minutes >= 60 or minutes < 0):
			should_validate_next = False
			
	except ValueError:
		should_validate_next = False
		
print (should_validate_next)