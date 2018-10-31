def array_dif_v1(first_array, second_array):
    """
        This version accumulates result by checking every number
        in first array for presence in second one
    """
    result = [element for element in first_array if not second_array.count(element)]

    return result


def array_dif_v2(first_array, second_array):
    """
        This version removes elements from copy of initial array
        def predicate(x) used instead of lambda to avoid complex expression in filter function call
    """
    result = first_array

    for element in second_array:

        def predicate(x):

            return bool(x != element)

        result = list(filter(predicate, result))

    return result


first_input_string = input('Enter first collection, please. Use "," as delimiter: ')
second_input_string = input('Enter second collection, please. Use "," as delimiter: ')

first_collection = first_input_string.split(',')
second_collection = second_input_string.split(',')

print(array_dif_v1(first_collection, second_collection))
print(array_dif_v2(first_collection, second_collection))
