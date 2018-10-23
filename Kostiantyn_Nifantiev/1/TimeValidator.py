while True:

    time_to_validate = input('Enter time to validate: ')
    time_to_validate = time_to_validate.strip()
    tokens = time_to_validate.split(':')

    if len(tokens) == 2 and tokens[0].isnumeric() and tokens[1].isnumeric():
        
        hours = int(tokens[0])
        minutes = int(tokens[1])
        
        if hours >=0 and hours < 24 and minutes >=0 and minutes < 60:

            print('True')

        else:

            print('False')

    else:

        print('False')
