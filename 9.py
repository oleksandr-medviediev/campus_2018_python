print("Convert a 24-hour time to a 12-hour time.")
print("Time must be validated.")

user_input = input("Enter time: ")

formatted_time = str()

if len(user_input) != 5:

    print("not valid time")

hours = user_input[:2]
minutes = user_input[3:]

if hours.isnumeric() and minutes.isnumeric():
    
    hours_in_int = int(hours)
    minutes_in_int = int(minutes)
    
    if (hours_in_int < 0 or hours_in_int > 23) or (minutes_in_int < 0 or minutes_in_int > 59):

        print("not valid time")
        
    else:

        if hours_in_int > 12:

            formatted_time = '{:02d}:{:02d} pm'.format(hours_in_int - 12, minutes_in_int) 

        elif hours_in_int == 12:

            formatted_time = '12:{:02d} pm'.format(minutes_in_int) 

        elif hours_in_int == 0:

            formatted_time = '12:{:02d} am'.format(minutes_in_int) 

        else: 

            formatted_time = '{:02d}:{:02d} am'.format(hours_in_int, minutes_in_int) 

    print(formatted_time)
          
else:

    print("not valid time")
