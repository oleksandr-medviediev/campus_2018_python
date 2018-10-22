string = input("input your string: ")

is_yelling = string.isupper();

if len(string) == 0:
    print("Fine. Be that way!")
elif string[-1] == '?':
    if not is_yelling:
        print("Sure.")
    else:
        print("Whoa, chill out!")
elif string[-1] == '!':
    print("Calm down, I know what I'm doing!")
else:
    print("Whatever.")
