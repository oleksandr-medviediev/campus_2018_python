string = input('enter the string\n');
letters_map = {}

for i in range(len(string)):
    letter = string[i].capitalize()
    letters_map[letter] = letters_map.get(letter, 0) + 1;

letters_count = letters_map.values()
repeated_letters = [x for x in letters_count if x > 1]

is_isogram = len(repeated_letters) == 0
print(is_isogram)
