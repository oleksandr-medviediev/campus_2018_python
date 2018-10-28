
mstr = input()

# Yelling question
if mstr.isupper() and mstr.endswith('?'):
    # yelling
    print("Calm down, I know what I'm doing!")
elif mstr.isupper() and not mstr.endswith('?'):
    # yelling question
    print("Whoa, chill out!")
elif not mstr.isupper() and mstr.endswith('?'):
    # questiong
    print("Sure.")
elif mstr is "":
    print("Fine. Be that way!")
else:
    print("Whatever.")

