inStr = str(input())

if len(inStr) == 0 :
    print('Fine. Be that way!')
elif inStr.isupper() :
    if inStr.endswith('?') :
        print('Calm down, I know what I\'m doing!')
    else :
        print('Whoa, chill out!')
elif inStr.endswith('?') :
    print('Sure.')
else :
    print('Whatever.')

