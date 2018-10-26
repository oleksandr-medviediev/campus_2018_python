pin = input('Enter a pin: ')

print((len(pin) == 4 or len(pin) == 6) and pin.isdigit())
