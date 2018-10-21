str = input("enter smth\n").lower()
number_of_O = 0
number_of_X = 0


for i in str:
    if i == 'x':
        number_of_X = number_of_X + 1
    if i == 'o':
        number_of_O = number_of_O + 1 

print(number_of_O == number_of_X)
   
input()
