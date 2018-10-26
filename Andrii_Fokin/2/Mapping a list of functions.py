import math

def map_functions(val, *functions):
    result = list()

    for foo in functions:
        if getattr(foo, '__iter__', False):
            result += map_functions(val, *foo)        
        else:
            result.append(foo(val))

    return result

family_of_functions = [math.sin,  math.cos, math.tan]
print(map_functions(0, family_of_functions, math.tan))
