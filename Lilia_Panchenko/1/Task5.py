str = input('Please, enter some string:\n')
len_str = len(str)

if (len_str % 2 == 0):
	print(str[len_str // 2 - 1] + str[len_str // 2])
else:
	print(str[len_str // 2])