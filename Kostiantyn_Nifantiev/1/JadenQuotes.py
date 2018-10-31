while True:

    incoming_quote = input('Enter a sentence to Capitalize It, Please ')
    tokens = incoming_quote.split()

    for i in range(len(tokens)):

        tokens[i] = tokens[i].capitalize()

    outcoming_quote = ' '.join(tokens)
    print(outcoming_quote)
