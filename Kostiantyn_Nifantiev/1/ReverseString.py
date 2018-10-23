user_string = input('Enter your string, please')

#V1
#reverse_string = user_string[::-1]
#end of V1

#V2
reverse_string = ''
reverse_range = range(len(user_string) - 1, -1, -1)

for i in reverse_range: 
    
    reverse_string += user_string[i]

#end of V2

print(reverse_string)
