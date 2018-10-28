key = input("enter the key\n")
if key.isdigit():
    key = int(key)

if key <= 26:

    string = input("enter the string\n")

    char_list = []
    char_list.extend(string)

    for i in range(len(char_list)):
        char = char_list[i]
        if char.isalpha():
            ascii_code = ord(char)
            new_ascii_code = ascii_code + key

            if (char.islower() and new_ascii_code > ord('z')) or (char.isupper() and new_ascii_code > ord('Z')):
                new_ascii_code -= 26

            new_char = chr(new_ascii_code)
            char_list[i] = new_char

    string = ''.join(char_list)
    print(string)

else:
    print("the input is not valid")
