from pythontask8 import validate_24_hour

def convert_24_to_12(time_string):
    result_string = "not a valid time"
    if validate_24_hour(time_string):
        time_list = time_string.split(':')
        if(int(time_list[0]) < 12):
            result_string = time_string + " am"
        else:
            hours = int(time_list[0]) - 12
            result_string = '{}:{} pm'.format(hours,time_list[1])

    return result_string
        
