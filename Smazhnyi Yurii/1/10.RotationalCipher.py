shift = int(input("input shift: "))
string = input("input your string: ")

new_string = ""

for i in range(len(string)):
    int_value = ord(string[i])
    int_value += shift
    new_string += chr(int_value)

print(new_string)
