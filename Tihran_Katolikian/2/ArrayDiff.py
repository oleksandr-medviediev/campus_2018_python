def array_diff_first(list_to_be_filtered, filter_values):

    value_presence_filter = lambda x: x not in filter_values
    filtered_list = filter(value_presence_filter, list_to_be_filtered)
    return list(filtered_list)


def array_diff_second(list_to_be_filtered, filter_values):

    for value in filter_values:
        list_to_be_filtered = [x for x in list_to_be_filtered if x != value]
    return list_to_be_filtered


print(array_diff_second([1, 2, 2, 2, 3], [2]))
