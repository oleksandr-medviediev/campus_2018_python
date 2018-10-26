def substract_list(list1,list2):
    result_list = [x for x in list1 if x not in list2]
    return result_list

def substract_list_v2(list1,list2):
    result_list = list(filter(lambda x : x not in list2, list1))
    return result_list
