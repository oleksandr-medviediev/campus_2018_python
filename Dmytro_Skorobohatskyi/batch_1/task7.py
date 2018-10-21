str = input('enter the string\n')

answer = ""
if len(str) == 0:
    answer = "Fine. Be that way!"
elif str.endswith("?"):
    if str.isupper():
        answer = "Calm down, I know what I'm doing!"
    else:
        answer = "Sure."
elif str.isupper():
    answer = "Whoa, chill out!"
else:
    answer = "Whatever."

print(answer)
