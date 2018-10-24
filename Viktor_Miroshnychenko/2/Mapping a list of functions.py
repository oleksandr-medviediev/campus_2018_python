def map_functions(variable, functions):
    return_val = list()
    for func in functions:
        return_val.append(func(variable))

    return return_val


functions = [ lambda var: var + 2, lambda var: var - 2, lambda var: var / 2 ]

print(map_functions(4, functions))
