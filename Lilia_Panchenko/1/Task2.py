input_str = input('Please, enter some string:\n')

words = input_str.split()

for i in range(len(words)):
	words[i] = words[i].capitalize()

new_phrase = ' '.join(words)
	
print(new_phrase)
