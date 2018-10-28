def words_by_modulus( n, modulus ):
	"""
	creates list of words to spell rest of  n % modulus
	: param1 : n (int) 
	: param2 : modulus (int)  
	: return : True if n % modulus not 0 and spell of n%modulus
	: rtype : tuple (bool, str)
	"""
	WORDS_DIGIT = { 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
	6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine' }
	
	WORDS_TEN_TO_TWENTY = { 10 : 'ten', 11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
	15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen', 19 : 'nineteen'}
	
	WORDS_TENS = { 20 : 'twenty', 30 : 'thirty', 40 : 'fourty', 50 : 'fifty',
	60 : 'sixty', 70 : 'seventy', 80 : 'eighty', 90 : 'ninety'}
	
	was_added = False	
	n = n % modulus
	if n > 0:
		was_added = True
	words = []
	
	if n < 10:
		word = str(WORDS_DIGIT[n])
		
	elif n < 20:
		word = str(WORDS_TEN_TO_TWENTY[n])
		
	else:		
		word = str(WORDS_TENS[n - n % 10]) + '-' + str(WORDS_DIGIT[n % 10])
		
	return was_added, word
	

HUNDRED = 'hundred'

MODULUSES = {0 : 100, 1 : 10}

WORDS_ZEROS = {
1 : 'thousand',
2 : 'million',
3 : 'billion'
}

input_str = input("Enter your number, please: \n")

valid_input = input_str.isdigit()
if valid_input:	
	n = int(input_str)
	
else :
	output_str = 'Invalid input!'
	n = 0
	
words = []

digits_passed = 0
zeros = 0
zeros_add = 0

while n > 0:
	
	modulus = MODULUSES[digits_passed]
	digits_added, words_added = words_by_modulus(n, modulus)
	
	if digits_passed == 0: 
		if zeros in WORDS_ZEROS.keys():
			words.append(str(WORDS_ZEROS[zeros]))
		zeros += 1
		
	elif digits_passed == 1 and digits_added:
		words.append(HUNDRED)

	words.append(words_added)	
	digits_passed = (digits_passed + 1) % 2
	n //= modulus

words.reverse()
output_str = ' '.join(words)

print(output_str)
