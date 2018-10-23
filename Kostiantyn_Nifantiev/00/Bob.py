while True:

    statement = input('Say something to Bob: ')
    statement = statement.strip()
    
    if len(statement) < 1:

        print('Fine. Be that way!')

    elif statement.endswith('?'):

        if statement.isupper():
        
            print('Calm down, I know what I\'m doing!')
        
        else:

            print('Sure.')
    else:

        if statement.isupper():
        
            print('Whoa, chill out!')
        
        else:

            print('Whatever.')
