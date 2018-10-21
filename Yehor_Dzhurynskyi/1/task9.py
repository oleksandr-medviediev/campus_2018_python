from string_is_24_hour_time import string_is_24_hour_time

time24 = input('Enter 24-hour time string: ')

if string_is_24_hour_time(time24):
    time_parts = time24.partition(':')
    hours = int(time_parts[0])
    minutes = int(time_parts[2])

    noon = 'pm' if hours >= 12 else 'am'
    print('%.2d:%.2d %s' % (hours % 12, minutes, noon))
    
else:
    print('not a valid time')    
