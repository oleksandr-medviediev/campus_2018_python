import string

def bob_function(input_string):
    answer_string = ""
    if(input_string.isupper()):
        if(input_string.endswith('?')):
            answer_string = "Calm down, I know what I'm doing!"
        else:
            answer_string = "Whoa, chill out!"
    else:
        if input_string.endswith('?'):
            answer_string =  "Sure."
        else:
            if not input_string:
                answer_string = "Fine. Be that way!"
            else:
                answer_string = "Whatever."

    return answer_string

