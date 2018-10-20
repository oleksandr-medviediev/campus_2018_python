sentence = input('Talk to Bob:')

def respond_like_bob (sentence):
    if not sentence:
        return "Fine. Be that way!"

    is_question = sentence[len(sentence) - 1] == '?'
    yelling = sentence.isupper()
    
    if yelling and is_question:
        return "Calm down, I know what I'm doing!"
    elif yelling:
        return "Whoa, chill out!"
    elif is_question:
        return "Sure."

print(respond_like_bob(sentence))
    
