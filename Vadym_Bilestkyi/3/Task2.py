from math import sqrt


def encode(sentence):
    sentence = sentence.strip().casefold()
    sentence = ''.join(letter for letter in sentence if letter.isalnum())

    square_root = sqrt(len(sentence))
    fractional_part = square_root - int(square_root)
    rows_number = columns_number = 0

    if fractional_part == 0:
        rows_number = columns_number = int(square_root)
    elif fractional_part < 0.5:
        rows_number = int(square_root)
        columns_number = rows_number + 1
    else:
        rows_number = columns_number = int(square_root) + 1

    rows = [sentence[i:i + columns_number] for i in range(0, len(sentence), columns_number)]
    missed = len(rows[0]) - len(rows[-1])
    if missed:
        rows[-1] += ' ' * missed

    column_join = lambda column: ''.join(letter for letter in column if not letter.isspace())
    encoded = ''.join(column_join(column) for column in zip(*rows))
    return encoded

print(encode('   If man was meant to stay on the ground, god would have given us roots.   '))
