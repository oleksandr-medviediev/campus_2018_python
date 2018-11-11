
def get_input(predicate, input_message):
    """
    Gets input from user satisfying given predicate
    :param predicate: Predicate, accepts string, returns tuple of Bool and string (error message)
    :param input_message: Message to display user
    :return: Accepted string
    """

    return_string = ""
    while True:

        string = input(input_message)
        predicate_result, predicate_error_string = predicate(string)

        if predicate_result:

            return_string = string
            break
        else:
            print(predicate_error_string)

    return return_string


def vector_sum(lhs, rhs):
    """
    Calculates sum of XY vector
    :param lhs: Tuple/List containing X and Y coordinates as index 0 and 1
    :param rhs: Tuple/List containing X and Y coordinates as index 0 and 1
    :return: List containing X and Y sum
    """
    return [lhs[0] + rhs[0], lhs[1] + rhs[1]]
