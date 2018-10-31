while True:

    time_to_validate = input('Enter time to convert: ')
    time_to_validate = time_to_validate.strip()
    tokens = time_to_validate.split(':')

    if len(tokens) == 2 and tokens[0].isnumeric() and tokens[1].isnumeric():
        
        hours = int(tokens[0])
        minutes = int(tokens[1])
        
        if hours >=0 and hours < 24 and minutes >=0 and minutes < 60:
            am_pm_indicator = ''
            
            if hours < 12:

                am_pm_indicator = ' am'
            
            else:

                hours -= 12
                
                if hours == 0:
                
                    hours = 12

                tokens[0] = str(hours)
                am_pm_indicator = ' pm'
            
            converted_time = ':'.join(tokens) + am_pm_indicator
            print(converted_time)

        else:

            print('Wrong time!')

    else:

        print('Wrong input!')
