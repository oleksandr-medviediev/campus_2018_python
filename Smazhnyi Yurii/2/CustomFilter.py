def custom_filter(condition, sequence):

    """Just Custom filter()"""

    output = []

    for i in sequence:
        if(condition(i)):
            output.append(i)
    
    return output


number_list = range(-5, 5)
less_than_zero = list(custom_filter(lambda x: x < 0, number_list))

print(less_than_zero)
