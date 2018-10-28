

def custom_filter(func, iterable):
    """
    Implementation of filter function

    Args:
        func (function): Filter function.
        iterable (iterable object): Iterable object.

    Returns:
        Filtered list.
    """
    if func is None:
        return [i for i in iterable]
    return [i for i in iterable if func(i)]


if __name__ == "__main__":
    func = lambda x: x % 2 == 0
    example_data = [1, 2, 3, 4]
    print("example for function x % 2 == 0 with list: " + str(example_data))
    print(custom_filter(func, example_data))
