is_valid_pin = lambda pin: len(pin) in (4, 6) and pin.isdigit()


print(is_valid_pin('1234'))
print(is_valid_pin('12345'))
print(is_valid_pin('a234'))
print(is_valid_pin('123456'))
