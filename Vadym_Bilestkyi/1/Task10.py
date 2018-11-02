alphabet = 'abcdefghijklmnopqrstuvwxyz'


def encode(shift, sentence):
    words = sentence.lower().split()
    encoded_words = []
    for word in words:
        encoded_letters = map(lambda letter: alphabet[(alphabet.find(letter) + shift) % len(alphabet)], word)
        encoded_word = ''.join(encoded_letters)
        encoded_words.append(encoded_word)

    encoded_sentence = ' '.join(encoded_words)
    return encoded_sentence


print(encode(13, 'The quick brown fox jumps over the lazy dog.'))
