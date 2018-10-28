import string
def jaden_string_convert(original_string):
    words_list = original_string.split(" ")
    for i in range(len(words_list)):
        words_list[i] = words_list[i].capitalize()
    result_string = ' '.join(words_list)
    
    return result_string
