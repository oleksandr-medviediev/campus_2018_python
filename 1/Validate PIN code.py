pin_code = input("PIN:\n")

if len(pin_code) == 4 or len(pin_code) == 6:
    for i in pin_code:
        if not i.isdigit():
            print("false")
            break
    else:
        print("true")
else:
    print("false")
    
input()