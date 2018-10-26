def array_dif_v1(first_array, second_array):
    """
        This version accumulates result by checking every number
        in first array for presence in second one
    """
    result = list()

    for element in first_array:

        if not second_array.count(element): result += element

    return result

def array_dif_v2(first_array, second_array):
    """
        This version removes elements from copy of initial array
    """
    result = set(first_array)

    for element in second_array: 
        try: result.remove(element)
        except: continue

    return result


first_input_string = input('Enter first collection, please. Use "," as delimiter: ')
second_input_string = input('Enter second collection, please. Use "," as delimiter: ')

first_collection = first_input_string.split(',')
second_collection = second_input_string.split(',')

print(array_dif_v1(first_collection, second_collection))
print(array_dif_v2(first_collection, second_collection))
print(first_collection)
input()
