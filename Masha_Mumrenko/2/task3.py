def custom_map(function, *args):
    length_list = [len(arg) for arg in args]
    min_length = min(length_list)
    
    result = []
    for index in range(min_length):
        parameters_list = []
        
        for arg in args:
            parameters_list.append(arg[index])
        
        result.append(function(*parameters_list))
        
    return result
