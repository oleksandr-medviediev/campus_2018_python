print("Convert strings to how they would be written by Jaden Smith.")
print("The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.")

user_input = input("Enter quote: ")

words = user_input.split()
capitalized_words = []

for x in words:
    
    temp = x.capitalize()
    capitalized_words.append(temp)

output_string = ' '.join(capitalized_words)

print(output_string)
