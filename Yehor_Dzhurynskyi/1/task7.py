string = input('Enter string: ')

is_yell_question = string.endswith('?!') or (string.endswith('?') and string.isupper())

if is_yell_question:
    print('Calm down, I know what I\'m doing!')
elif string.endswith('?'):
    print('Sure.')
elif string.endswith('!'):
    print('Whoa, chill out!')
elif len(string.strip()) == 0:
    print('Fine. Be that way!')
else:
    print('Whatever.')

