
def isTime(HM):
    result = True
    if len(HM) != 2 or HM[0].isnumeric() == False or HM[1].isnumeric() == False :
        result = False
    else :
        result = (int(HM[0]) < 24 and int(HM[1]) < 60)
    return result

time = input().split(':')
if isTime(time):
    hours = int(time[0]) % 12
    minutes = int(time[1])

    l = lambda : 'pm' if int(time[0]) > hours else 'am'
    answer = f"{str(hours).zfill(2)}:{minutes} {l()}"
else:
    answer = 'not a valid time'

print(answer)
