import math

def map_functions(arg, *functions):
    for func in functions:
        arg = func(arg)
    return arg

num = float(input("Enter number\n"))
print(map_functions(num, math.sin, math.cos))
