def custom_range(*args):
    """
    Yield sequence of integers, generated according to arguments.

    Possible prototypes:
    custom_range(stop)
    custom_range(start, stop)
    custom_range(start, stop, step)

    :param args:    start - starting value of the resulting sequence (inclusive, defaults to 0).
                    stop - ending value of the resulting sequence (exclusive).
                    step - step of the sequence (defaults to 0).
    :type args: int.

    :yield: sequence of integers.
    :yield type: int.
    """
    if len(args) == 1:
        start, stop, step = (0, *args, 1)
    elif len(args) == 2:
        start, stop, step = (*args, 1)
    elif len(args) == 3:
        start, stop, step = args
    else:
        raise TypeError(f'Expected from 1 to 3 arguments, got {len(args)}.')

    if step < 0:
        def comparison(a, b): return a > b
    elif step > 0:
        def comparison(a, b): return a < b
    else:
        raise ValueError('Expected step, different from 0.')

    while comparison(start, stop):
        yield start
        start += step


arguments = (10, 100, 5)

print(list(custom_range(*arguments)))
print(list(range(*arguments)))
