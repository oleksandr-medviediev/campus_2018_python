print("Given a person's allergy score, determine whether or not they're allergic to a given item, and their full list of allergies.")

allergies = {'1': "eggs", '2': "peanuts", '4': "shellfish",
 '8': "strawberries", '16': "tomatoes", '32': "chocolate", '64': "pollen", '128': "cats"}

max_allergen = 128

def process_allergies(arg, next_allergen, determined_allergies):
    
    new_determined_allergies = determined_allergies
    
    if arg == 0:

        return new_determined_allergies

    elif arg // next_allergen == 1:

        new_determined_allergies.append(allergies.get(str(next_allergen)))

        return process_allergies(arg % next_allergen, next_allergen // 2, determined_allergies)

    else:

        return process_allergies(arg, next_allergen // 2, determined_allergies)



def determine_allergies(arg):

    determined_allergies = []

    if arg // max_allergen > 1:

        return process_allergies(arg % max_allergen, max_allergen // 2, determined_allergies)

    else:

        return  process_allergies(arg, max_allergen, determined_allergies)


user_input = input("Enter allergy score: ")

if user_input.isnumeric():

    user_input_int = int(user_input)

    found_allergies = determine_allergies(user_input_int)

    if len(found_allergies) == 0:

        found_allergies.append(None)

    print(found_allergies)
