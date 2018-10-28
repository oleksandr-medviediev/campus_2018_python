def allergies(allergy_sum):
    allergy_list = ["eggs","peanuts","shellfish","strawberries","tomatoes","chocolate","pollen","cats"]
    current_index = 0
    result = []
    
    while allergy_sum != 0 and current_index < len(allergy_list):
        allergy_to_item = allergy_sum & 1
        
        if allergy_to_item:
            result.append(allergy_list[current_index])
            
        allergy_sum = allergy_sum >> 1
        current_index += 1

    return result
