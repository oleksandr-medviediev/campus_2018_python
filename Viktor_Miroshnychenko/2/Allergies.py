def find_allergis(total_score):
    aler_score = [1,2,4,8,16,32,64,128]
    aler_names = ["eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"]
    aler_score.reverse()
    aler_names.reverse()

    return_val = list()
    for i in range(len(aler_score)):
        if aler_score[i] <= total_score:
            return_val.append(aler_names[i])
            total_score -= aler_score[i]

    return return_val


print(find_allergis(93))
    
