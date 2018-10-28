number = int(input())

list_of_ingridients = ["eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"]

output_list = [item for index, item in enumerate(list_of_ingridients) if number & (2**index) != 0]

print(", ".join(output_list))

