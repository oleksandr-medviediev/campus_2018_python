input_str = input('Please, input some string:\n')
input_len = len(input_str)

case_insensitive_input = input_str.casefold();

letters = {i:case_insensitive_input.count(i) for i in case_insensitive_input}
		
print (letters['o'] == letters['x'])		
