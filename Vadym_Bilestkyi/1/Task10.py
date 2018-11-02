alphabet = 'abcdefghijklmnopqrstuvwxyz'


def encode(shift, sentence):
    words = sentence.lower().split()
    return ' '.join(''.join(
        map(
            lambda letter: alphabet[(alphabet.find(letter) + shift) % len(alphabet)],
            word
        )
    ) for word in words)


print(encode(13, 'The quick brown fox jumps over the lazy dog.'))
