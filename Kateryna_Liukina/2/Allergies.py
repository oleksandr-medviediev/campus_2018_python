def determine_allergies(number):
    """Return list of allergies that contain number"""
    list_of_allergies = ["eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"]
    output_list = [item for index, item in enumerate(list_of_allergies) if number & (2**index) != 0]

    return output_list
