def array_diff_first(list_to_be_filtered, filter_values):
    """
    Removes all elements in list_to_be_filtered which present in
    filter_values

    :param list_to_be_filtered: list which is going to be filtered
    :param filter_values: list with values that will be deleted if present in the
    list_to_be_filtered
    :return: filtered list_to_be_filtered
    """

    value_presence_filter = lambda x: x not in filter_values
    filtered_list = filter(value_presence_filter, list_to_be_filtered)
    return list(filtered_list)


def array_diff_second(list_to_be_filtered, filter_values):
    """
    Removes all elements in list_to_be_filtered which present in
    filter_values

    :param list_to_be_filtered: list which is going to be filtered
    :param filter_values: list with values that will be deleted if present in the
    list_to_be_filtered
    :return: filtered list_to_be_filtered
    """

    for value in filter_values:
        list_to_be_filtered = [x for x in list_to_be_filtered if x != value]
    return list_to_be_filtered


print(array_diff_second([1, 2, 2, 2, 3], [2]))
