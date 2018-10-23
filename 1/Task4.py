input_str = input('Please, input some phrase to check if it is an isogram:\n')
len_input = len(input_str)

letters = ''

for i in range(len_input):
	char = input_str[i]
	is_alpha = char.isalpha()
	is_in_letters = char in letters
	if (not is_in_letters and is_alpha):
		letters = letters + char
		
	if is_in_letters:
		break

print(not is_in_letters)
