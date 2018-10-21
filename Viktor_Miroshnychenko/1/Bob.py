import sys

replic_to_bob = input("Speak to Bob \n")

if replic_to_bob == "":
    print("Fine. Be that way!")
    sys.exit()

last_char = replic_to_bob[-1]
pre_last_char = replic_to_bob[-2]

if last_char == "?":
    if pre_last_char == "!":
        print("Calm down, I know what I'm doing!")
    else:
        print("Sure")
elif last_char == "!":
    if pre_last_char == "?":
        print("Calm down, I know what I'm doing!")
    else:
        print("Whoa, chill out!")
else:
    print("Whatever.")

