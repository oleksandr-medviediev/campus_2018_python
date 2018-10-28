import string
def is_isogram(original_string):
    lower_case_string = original_string.lower()
    for char in lower_case_string:
        if(char.isalpha() and lower_case_string.count(char) > 1):
            return False

    return True

