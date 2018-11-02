def evaluate_bobby(request):
    if request:
        if request[-1] == '?':
            if request.isupper():
                return 'Calm down, I know what I\'m doing!'
            else:
                return 'Sure.'
        elif request[-1] == '!' or request.isupper():
            return 'Whoa, chill out!'
        elif 'Bob' in request:
            return 'Fine. Be that way!'

    return 'Whatever.'


print(evaluate_bobby('What a f*ck?'))
print(evaluate_bobby('WHAT THE F*CK?'))
print(evaluate_bobby('Hi, Bob.'))
print(evaluate_bobby(''))
