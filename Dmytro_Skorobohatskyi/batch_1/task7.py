string = input('enter the string\n')

answer = ""
if len(string) == 0:
    answer = "Fine. Be that way!"
elif string.endswith("?"):
    if string.isupper():
        answer = "Calm down, I know what I'm doing!"
    else:
        answer = "Sure."
elif string.isupper():
    answer = "Whoa, chill out!"
else:
    answer = "Whatever."

print(answer)
