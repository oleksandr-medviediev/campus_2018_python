time = input("enter time in 24 format\n")

numbers = time.split(":")
number_set = set(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"))
is_time = True

if len(numbers) != 2:
    is_time = False
else:
    for number in numbers:
        for i in number:
            if i not in number_set:
                is_time = False
                break
if is_time:
    is_time = int(numbers[0]) < 24 and int(numbers[0]) >= 0
    is_time = int(numbers[1]) < 60 and int(numbers[1]) >= 0

if is_time:
    if int(numbers[0]) > 12:
        print(str(int(numbers[0]) - 12) + ":" + numbers[1] + " pm")
    else:
        print(numbers[0] + ":" + numbers[1] + " am")
else:
    print("not a valid time")
    
            
input()