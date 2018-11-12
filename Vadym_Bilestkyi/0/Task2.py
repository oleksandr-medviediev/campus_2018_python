def read_file_gen(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line


for line in read_file_gen('FileForTask2'):
    print(line)
