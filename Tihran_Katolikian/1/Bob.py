s = input('Your talk to a Bob: ')

questionResponse = 'Sure.'
yellingResponse = 'Whoa, chill out!'
yellingQuestionResponse = 'Calm down, I know what I\'m doing!'
responseOnNothing = 'Fine. Be that way!'
universalResponse = 'Whatever'

if len(s) == 0:
    print(responseOnNothing)
elif len(s) >= 2 and (s[-3:-1] == '?!' or s[-3:-1] == '!?'):
    print(yellingQuestionResponse)
elif s[-1] == '!':
    print(yellingResponse)
elif s[-1] == '?':
    print(questionResponse)
else:
    print(universalResponse)
