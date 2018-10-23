import math


def map_functions(value, *list_of_functions):
    
    """Take value and apply list of functions to it. Returns list of outputs."""

    output_list = []

    for func in list_of_functions:

        output_list.append(func(value))
    
    return output_list
          

functions_to_apply = ( math.sin, math.cos, math.tan)

output = map_functions(3.14,  *functions_to_apply)

print(output)
