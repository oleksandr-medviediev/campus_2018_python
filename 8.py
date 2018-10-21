print("Validate a 24 hours time string.")

user_input = input("Enter time: ")

if len(user_input) != 5:
    print(False)

else:
    hours = int(user_input[:2])
    minutes = int(user_input[3:])

    if hours < 0 or hours > 23:
        print(False)

    elif minutes < 0 or minutes > 59:
        print(False)
        
    else:
        print(True)
