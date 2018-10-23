input_str = input('Please, enter some string:\n')
len_str = len(input_str)

middle_index = len_str // 2;

result = ''
if (len_str % 2 == 0):
	result += input_str[middle_index - 1]

result += input_str[middle_index]

print(result)
