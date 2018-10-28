import string


def rotate(iterable, shift):
    return iterable[shift:] + iterable[:shift]

shift = int(input('Enter shift: '))
source = input('Enter text to ciper: ')

rotated_lowercase = rotate(string.ascii_lowercase, shift)
rotated_uppercase = rotate(string.ascii_uppercase, shift)

lowercase_trantab = source.maketrans(string.ascii_lowercase, rotated_lowercase)
uppercase_trantab = source.maketrans(string.ascii_uppercase, rotated_uppercase)

cipher = source.translate(lowercase_trantab).translate(uppercase_trantab)

print(cipher)
