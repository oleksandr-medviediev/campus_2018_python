def list_difference1(filter_list, target):
    for lvalue in filter_list:
        if lvalue in target:
            target.remove(lvalue)

    return target
    

input_list = list(input("Enter target list \n"))
filter_list = list(input("Enter filter list \n"))

print(list_difference1(filter_list, input_list))
