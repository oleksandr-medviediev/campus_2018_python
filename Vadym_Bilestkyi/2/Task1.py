def find_odd1(numbers):
    for number1 in numbers:
        count = 0
        for number2 in numbers:
            if number1 == number2:
                count += 1
        if count % 2 == 1:
            return number1

    return None


def find_odd2(numbers):
    for number in numbers:
        if numbers.count(number) % 2 == 1:
            return number

    return None


def find_odd3(numbers):
    numbers_amount = {}
    for number in numbers:
        numbers_amount[number] = numbers_amount.get(number, 0) + 1

    for number, amount in numbers_amount.items():
        if amount % 2 == 1:
            return number

    return None


print('First way:', find_odd1([1, 2, 3, 2, 1]))
print('Second way:', find_odd2([1, 2, 3, 2, 1]))
print('Third way:', find_odd3([1, 2, 3, 2, 1]))
