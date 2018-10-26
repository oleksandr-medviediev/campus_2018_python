HM = input().split(':')

def isTime(HM):
    result = True
    if len(HM) != 2 or HM[0].isnumeric() == False or HM[1].isnumeric() == False :
        result = False
    else :
        result = (int(HM[0]) < 24 and int(HM[1]) < 60)
    return result

print(isTime(HM))
