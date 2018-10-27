input_string = input("Enter a string\n")

map_of_answers =  {"Yell":{"?": "Calm down, I know what I'm doing!", ".": "Whoa, chill out!"}, \
                   "Say": {"?": "Sure.", ".": "Whatever."}, \
                   "Silence": "Fine. Be that way!"}

input_string = input_string.replace(" ", "")

if len(input_string) == 0:
    print (map_of_answers["Silence"])
elif not input_string.isupper():

    if (input_string.find("?") != -1):
        print(map_of_answers["Say"]["?"])
    else:
        print(map_of_answers["Say"]["."])
else:

    if(input_string.find("?") != -1):
        print (map_of_answers["Yell"]["?"])
    else:
        print (map_of_answers["Yell"]["."])
