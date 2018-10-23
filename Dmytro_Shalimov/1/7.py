print("Bob is a lackadaisical teenager. In conversation, his responses are very limited.")
print("Bob answers \"Sure.\" if you ask him a question.")
print("He answers \"Whoa, chill out!\" if you yell at him.")
print("He answers \"Calm down, I know what I'm doing!\" if you yell a question at him.")
print("He says \"Fine. Be that way!\" if you address him without actually saying anything.")
print("He answers \"Whatever.\" to anything else.")

user_input = input("Say something to Bob: ")

if len(user_input) == 0:
    print("Fine. Be that way!")

elif user_input[-1] == '?':
    if user_input[-2].isupper():
        print("Calm down, I know what I'm doing!")
        
    else:
        print("Sure")

else:
    if user_input[-1].isupper():
        print("Whoa, chill out!")

    else:
        print("Whatever.")
