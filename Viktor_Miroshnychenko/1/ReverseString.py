string = input("Type a string to reverse \n")

result2 = ""
for iter in range(len(string)):
    result2 += string[-iter - 1]

print(result2)
