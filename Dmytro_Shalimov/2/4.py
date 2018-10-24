print("Write a function which applies a bunch of functions, which may be an iterable such as a list, for example, to one Python object.")

def apply_functions_to_object(functions, arg):

    new_list = []

    for x in functions:

        new_list.append(x(arg))
    
    return new_list


func_pow2 = lambda x: x ** 2
func_pow3 = lambda x: x ** 3
func_pow4 = lambda x: x ** 4

func_list = [func_pow2, func_pow3, func_pow4]

user_input = input("Enter number: ")

if user_input.isnumeric():

    print(apply_functions_to_object(func_list, int(user_input)))
