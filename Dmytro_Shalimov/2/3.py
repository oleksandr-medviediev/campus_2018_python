print("Implement custom_map function, which will behave like the original Python map() function.")



def my_map(functor, list_arg):

    new_list = []

    for x in list_arg:

        new_list.append(functor(x))

    return new_list



def double_func(arg):

    return arg + arg



user_input = input("Enter sequence using spaces: ")
numbers_list = list(map(int, user_input.split()))

print(list(my_map(double_func, numbers_list)))
