str = input('Please, enter some string:\n')
len_str = len(str)

middle_index = len_str // 2;

result = ''
if (len_str % 2 == 0):
	result += str[middle_index - 1]

result += str[middle_index]

print(result)
