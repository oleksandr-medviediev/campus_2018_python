input_str = input('Please, input some string:\n')
input_len = len(input_str)

balance = 0

for i in range(input_len):
	if (input_str[i] == 'x' or input_str[i] == 'X'):
		balance += 1
	elif (input_str[i] == 'o' or input_str[i] == 'O'):
		balance -= 1
		
print (balance == 0)		