def custom_map(func, *list_of_inputs):

    """
    Custom map(). For Documentation read map() doc

    @param func: function to apply
    @param *list_of_inputs: lits that will be taked as parameters for function
    @returns: list of function's results
    """

    output = []
    min_length = len(min([test_list, test_list2], key=lambda sequence: len(sequence)))
    arguments_lists = []

    for i in range(min_length):

        arguments_lists.append([])

        for sequence in list_of_inputs:

            arguments_lists[i].append(sequence[i])
            
    for i in range(min_length):

        output.append(func(*arguments_lists[i]))
    
    return output


test_list = [1, 2, 3, 4, 5, 6, 2, 3, 3, 1]
test_list2 = [1, 2, 3, 4, 6, 2, 3, 3, 1]

output = custom_map(lambda x,y: x*y, test_list, test_list2)

print(output)
