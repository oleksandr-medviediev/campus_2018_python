import string

input_str = input('Your message: ')

for_question = 'Sure.'
for_yelling = 'Whoa, chill out!'
for_yelling_question = "Calm down, I know what I'm doing!"
for_saying_anything = 'Fine. Be that way!'
whatever = 'Whatever.'

is_question = False
if ('?' in input_str):
	is_question = True
	
is_yelling = True
has_letters = False

for i in range(len(input_str)):
	symbol = input_str[i]
	
	is_letter = (symbol in string.ascii_letters)
	is_uppercase = (symbol in string.ascii_uppercase)
	
	if (is_letter):
		has_letters = True
		
		if (not is_uppercase):
			is_yelling = False

if (not has_letters):
	print(for_saying_anything)
	
elif (is_question):
	
	if (is_yelling):
		print(for_yelling_question)
		
	else:
		print(for_question)
		
elif (is_yelling):
	print(for_yelling)
	
else:
	print(whatever)
	
	
	
	