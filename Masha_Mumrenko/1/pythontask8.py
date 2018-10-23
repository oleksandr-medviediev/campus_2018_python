def validate_24_hour(hour_string):
    validation_list = [24,60]
    answer = True
    string_parts = hour_string.split(':')
    if len(string_parts) != 2:
        answer = False
    else:
        for i in range(len(string_parts)):
            if int(string_parts[i]) >= validation_list[i] or int(string_parts[i]) < 0:
                answer = False
                break

    return answer
