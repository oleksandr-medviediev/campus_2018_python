input_string = input("input a string that has to be Jaden Cased: ")

resulting_string = str()
input_words = input_string.split()

for word in input_words:
    resulting_string += word.capitalize() + ' '

print(resulting_string)
