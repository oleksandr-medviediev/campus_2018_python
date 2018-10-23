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


is_yelling = input_str.isupper()
has_letters = input_str.islower() or is_yelling

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
