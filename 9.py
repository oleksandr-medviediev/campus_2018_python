print("Convert a 24-hour time to a 12-hour time.")
print("Time must be validated.")

user_input = input("Enter time: ")

formatted_time = []
is_am = False

if len(user_input) != 5:
    print("not valid time")

else:
    hours = int(user_input[:2])
    minutes = int(user_input[3:])

    if hours < 0 or hours > 23:
        print("not valid time")

    elif minutes < 0 or minutes > 59:
        print("not valid time")

    else:
        if hours > 12:    
            formatted_time.append(str(hours - 12))

        else:
            is_am = True
            formatted_time.append(str(hours))

        formatted_time.append(str(minutes))
        formatted_time_string = ':'.join(formatted_time)

        if is_am == True:
            print(formatted_time_string + " am")
            
        else:
            print(formatted_time_string + " pm")
