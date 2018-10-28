import string
def get_middle_character(word):
    answer = ""
    if(len(word)%2 == 0 and len(word)!=0):
        answer = word[len(word)/2 - 1] + word[len(word)/2]
    else:
        answer = word[len(word)/2]

    return answer
