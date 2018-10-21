string = input('Enter string: ')

string
for ch in string:
    if ch.isalpha and string.count(ch) != 1:
        print(False)
        break
else:
     print(True)   
        
