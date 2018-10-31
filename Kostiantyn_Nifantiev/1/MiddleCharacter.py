incoming_string = input('Enter your string, please: ')

length_of_string = len(incoming_string)
middle_index = int(length_of_string / 2)

if length_of_string % 2:

    print(incoming_string[middle_index])

else:

    print(incoming_string[middle_index - 1 : middle_index + 1])
