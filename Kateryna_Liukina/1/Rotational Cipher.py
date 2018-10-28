key_str = input("Enter a key\n")

if not key_str.isnumeric():
    print("Wrong key")
    quit()

key = int(key_str)

input_string = input('Enter a string\n')

numbers = [ord(ch) for ch in input_string]

for i in range(len(numbers)):
    if ord('a') <= numbers[i] < ord('a') + 27:
        numbers[i] = ord('a') + (numbers[i] - ord('a') + key) % 27
    elif ord('A') <= numbers[i] < ord('A') + 27:
        numbers[i] = ord('A') + (numbers[i] - ord('A') + key) % 27

chars = [chr(number) for number in numbers]

print(''.join(chars))
