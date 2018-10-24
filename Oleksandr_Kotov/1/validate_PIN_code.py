pin_code = input("type pin code: ")

length_validation = len(pin_code) == 4 or len(pin_code) == 6

print(length_validation and pin_code.isdigit())