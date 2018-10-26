def is_atm_pin(string_to_check):
    answer = False
    if(string_to_check.isdigit() and (len(string_to_check)== 4
                                      or len(string_to_check)== 6)):
        answer = True

    return answer
