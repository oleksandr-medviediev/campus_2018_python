def map_functions(subject, *args):
    """
    applies functions to element
        :param subject: any value which will be delegated into each function
        :param *args: functions which should be applied to `subject`
        :return: collection of `*args` results
    """

    results = [func(subject) for func in args]

    return results
