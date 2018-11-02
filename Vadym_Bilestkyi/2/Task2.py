def array_diff1(array1, array2):
    result = array1[:]
    for element in array2:
        while True:
            try:
                    result.remove(element)
            except ValueError:
                break

    return result


def array_diff2(array1, array2):
    result = []
    for element in array1:
        if element not in array2:
            result.append(element)

    return result


print(array_diff1([1, 2, 2, 2, 3], [2]))
print(array_diff2([1, 2, 2, 2, 3], [2]))
