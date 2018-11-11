from LineReader import gen_lines


example_file_name = 'some_text_file.txt'
for line in gen_lines(example_file_name):
    print(line)
