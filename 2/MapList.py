import math


def map_list(arg, *funcs):
    """
     Applies a bunch of functions, which may be an iterable.

     :param arg: function argument
     :param *funcs: iterable that contains functions to call
     :return: nothing
     :rtype: None
    """

    for foo in funcs[0]:
        foo(arg)


if __name__ == "__main__":
    functions_to_apply = (math.sin, math.cos, math.tan)
    map_list(3.14, functions_to_apply)
