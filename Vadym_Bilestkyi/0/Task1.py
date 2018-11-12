def gen_range(start, stop, step=1):
    if step == 0:
        raise ValueError('step must be nonzero value')

    while step > 0 and start < stop or step < 0 and start > stop:
        yield start
        start += step

print(list(gen_range(0, 5, 1)))
print(list(gen_range(0, 5, -1)))
print(list(gen_range(5, 0, -2)))
