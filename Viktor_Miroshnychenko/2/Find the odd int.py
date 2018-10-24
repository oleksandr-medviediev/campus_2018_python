input_list = input("Enter list of integers \n")

def find_odd_1(string):
    for char in string:
        if string.count(char) % 2 == 1:
            
            return char

def find_odd_2(string):
    list_of_odds = list(map(lambda char: string.count(char) % 2, string))
    odd_char = string[list_of_odds.index(1)]

    return odd_char

print(find_odd_1(input_list))
print(find_odd_2(input_list))
