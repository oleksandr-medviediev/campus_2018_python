print("Bob is a lackadaisical teenager. In conversation, his responses are very limited.")
print("Bob answers \"Sure.\" if you ask him a question.")
print("He answers \"Whoa, chill out!\" if you yell at him.")
print("He answers \"Calm down, I know what I'm doing!\" if you yell a question at him.")
print("He says \"Fine. Be that way!\" if you address him without actually saying anything.")
print("He answers \"Whatever.\" to anything else.")

user_input = input("Say something to Bob: ")

bob_answer_on_question = "Sure"
bob_answer_on_yell = "Whoa, chill out!"
bob_answer_on_yell_question = "Calm down, I know what I'm doing!"
bob_answer_on_nothing = "Fine. Be that way!"
bob_answer_on_everything_else = "Whatever."

if len(user_input) == 0:
    print(bob_answer_on_nothing)

elif user_input[-1] == '?':
    if user_input[-2].isupper() == True:
        print(bob_answer_on_yell_question)
        
    else:
        print(bob_answer_on_question)

else:
    if user_input[-1].isupper() == True:
        print(bob_answer_on_yell)

    else:
        print(bob_answer_on_everything_else)
    