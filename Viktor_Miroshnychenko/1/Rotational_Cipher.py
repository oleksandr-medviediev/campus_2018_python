import sys
string = input("Enter string to rotate \n")
shift = input("Enter rotation value \n")

shift = int(shift)

alph = "abcdefghijklmnopqrstuvwxyz"

rotated_string = ""

for char in string:
    iter = alph.find(char)
    iter = (iter + shift) % len(alph)
    rotated_string += alph[iter]

print(rotated_string)
