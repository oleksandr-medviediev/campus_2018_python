input_str = input('Please, input some phase to check if it is an isogram:\n')
len_input = len(input_str)

letters = ''

for i in range(len_input):
	is_space_or_hyphen = (input_str[i] == ' ' or input_str[i] == '-')
	is_in_letters = input_str[i] in letters
	if (not is_space_or_hyphen and not is_in_letters):
		letters = letters + input_str[i]
		
	if is_in_letters:
		break

print(not is_in_letters)