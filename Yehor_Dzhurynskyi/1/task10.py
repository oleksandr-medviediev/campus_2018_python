import string

def rotate(iterable, shift):
    return iterable[shift:] + iterable[:shift]

shift = int(input('Enter shift: '))
source_text = input('Enter text to ciper: ')

lowercase_trantab = source_text.maketrans(string.ascii_lowercase, rotate(string.ascii_lowercase, shift))
uppercase_trantab = source_text.maketrans(string.ascii_uppercase, rotate(string.ascii_uppercase, shift))

source_text = source_text.translate(lowercase_trantab)
print(source_text.translate(uppercase_trantab))


