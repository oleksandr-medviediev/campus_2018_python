print("Validate a 24 hours time string.")

user_input = input("Enter time: ")

if len(user_input) != 5:
    print(False)

hours = user_input[:2]
minutes = user_input[3:]

if hours.isnumeric() and minutes.isnumeric():
    
    hours_in_int = int(hours)
    minutes_in_int = int(minutes)
    
    if hours_in_int < 0 or hours_in_int > 23:
        print(False)

    elif minutes_in_int < 0 or minutes_in_int > 59:
        print(False)
        
    else:
        print(True)

else:

    print(False)
