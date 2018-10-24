first_arg_list = [1,2,3]
second_arg_list = [4,5,6,7]

def my_map(function, *containers):
    minLen = len(containers[0])
    for arg in containers:
        if minLen > len(arg):
            minLen = len(arg)

    func_arg_list = list()
    return_val = list()
    for i in range(minLen):
        for arg in containers:
            func_arg_list.append(arg[i])

        return_val.append(function(*func_arg_list))
        func_arg_list.clear()

    return return_val

print(my_map(lambda i, j: j / i, first_arg_list, second_arg_list))
