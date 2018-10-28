def bracket_type(bracket):
	BRACKES = { '(' : 1, ')' : 1, '{' : 2, '}' : 2, '[' : 3, ']' : 3 }
	br_type = BRACKETS [bracket] 
	
	return br_type


input_str = input("Enter your string, please: \n")

bracket_stack = []
for c in input_str:
	
	if c  in  [ '(', '[', '{' ]
		bracket_stack.append(c)
		
	if c in [ ')', ']', '}' ]
		
		if not len(bracket_stack) == 0 and bracket_type(c) == bracket_type(bracket_stack[-1]):
			bracket_stack.pop()
			
		else:
			bracket_stack.append(c)
		
print(len(bracket_stack) == 0)
