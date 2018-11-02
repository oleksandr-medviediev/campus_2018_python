def to_jaden_smith(quote):
    return ' '.join(word.capitalize() for word in quote.split())


if __name__ == '__main__':
    quote = input('Enter a sentence:')
    print(to_jaden_smith(quote))
