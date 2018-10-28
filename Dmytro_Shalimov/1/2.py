<<<<<<< HEAD
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
=======
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
>>>>>>> 715fd0763b415a13fb28a483f258a5eadc1ec931
