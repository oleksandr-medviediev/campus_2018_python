
def check_if_armstrong_number(num):
    result = 0
    num_in_str = str(num)
    for i in range(len(num_in_str)):
        result += int(num_in_str[i])**(len(num_in_str))
    return (num == result)

print(check_if_armstrong_number(10))
print(check_if_armstrong_number(9))