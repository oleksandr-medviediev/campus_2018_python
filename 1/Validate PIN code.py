pin_code = input("PIN:\n")

numbers = set(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"))
if len(pin_code)== 4 or len(pin_code)== 6:
    for i in pin_code:
        if i not in numbers:
            print("false")
            break
    else:
        print("true")
else:
    print("false")
    
input()