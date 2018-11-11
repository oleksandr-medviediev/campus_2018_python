from contextlib import contextmanager


def gen_lines(filename):
    '''
    Function is used to iterate throgh big files line by line.
    :param filename: a name of file to read;
    :return: a generator that yields lines of file;
    :type filename: str;
    :rtype: generator.
    '''
    with open (filename) as iterated_file:
        while True:
            line = iterated_file.readline()
            if line:
                yield line.rstrip()
            else:
                break
