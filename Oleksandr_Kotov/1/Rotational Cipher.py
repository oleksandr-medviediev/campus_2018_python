key = input("type key")

input_str = input("type str")

input_str = input_str.lower()

out_str = ""

for char in input_str:
    code = ord(char) + int(key)
    if code > ord('z'):
        code = ord('a') - 1 + (code - ord('z'))

    out_str += chr(code)

print(out_str)