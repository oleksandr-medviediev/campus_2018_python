def my_filter(function, container):
    """
    :param function: function that used as a filter to container
    :type function: function

    :param container: container that must be filtered
    :type container: any iterable container

    :return: filtered container
    :rtype: list
    """
    return_val = list()
    for var in container:
        if function(var):
            return_val.append(var)

    return return_val
            

a = [1,2,3,4]
b = [5,6,7,8,9]

print(list(filter(lambda i: i % 2, a)))
print(my_filter(lambda i: i % 2, a))
