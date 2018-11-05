def my_map(func, *iterables):
    """
    Calls given function on given container

    :param func: function to call
    :param *iterables: list of iterables that will be an arguments fo funcion call
    :return: nothing
    :rtype: None
    """

    argz = list(zip(*iterables[0]))

    for pack in argz:
        func(*pack)
      
      
if __name__ == "__main__":
    arr = [[1,2,3], [3,4,5], [3,4,5]]
    my_map(lambda x,y,z: print(x,y,z), arr)
