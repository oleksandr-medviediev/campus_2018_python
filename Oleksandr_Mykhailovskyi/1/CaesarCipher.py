import string

def Cypher(text, shift, alphabet = string.ascii_lowercase):
    shiftedAlph = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shiftedAlph)
    return text.translate(table)

def CaesarCypher(text, shift):
    shift %= 26 # for shifts > 26
    text = Cypher(text, shift)
    return Cypher(text, shift, string.ascii_uppercase)


shift = int(input("Enter shift\n"))
text = input("Enter text to cypher\n")
print(CaesarCypher(text, shift))