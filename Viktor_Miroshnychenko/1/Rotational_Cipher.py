string = input("Enter string to rotate \n")
shift = input("Enter rotation value \n")

shift = int(shift)

alph = "abcdefghijklmnopqrstuvwxyz"

rotated_string = ""

for char in string:
    position = alph.find(char)
    position = (position + shift) % len(alph)
    rotated_string += alph[position]

print(rotated_string)
