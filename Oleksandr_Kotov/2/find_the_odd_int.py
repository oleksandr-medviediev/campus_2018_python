def find_odd1(numbers):
    """function returns an alement with odd number of occurencies"""
    presences = {}   

    for number in numbers:

        presences.setdefault(number, 0)
        presences[number] +=1
    
    for number, presence in presences.items():
        if presence % 2 == 1:
            return number

def find_odd2(numbers):
    """function returns an alement with odd number of occurencies"""
    for number in numbers:
        count = 0
        
        for pretendent in numbers:
            if pretendent == number:  
                count +=1
                numbers.remove(pretendent)

        if count % 2 == 1:
            return number

def find_odd3(numbers):
    """function returns an alement with odd number of occurencies"""
    for number in numbers:
        if numbers.count(number) % 2 == 1:
            return number
