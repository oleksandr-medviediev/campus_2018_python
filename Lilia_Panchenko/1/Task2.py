str = input('Please, enter some string:\n')

words = str.split()
words_len = len(words)

new_phrase = ''

for i in range(words_len):
	new_phrase = new_phrase + words[i].capitalize() + ' '
	
print(new_phrase)