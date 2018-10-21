input_string = input("Enter string \n")

odd = bool(len(input_string)%2)

mid = int(len(input_string) / 2)
   
if odd == True:
   print(input_string[mid] )
else:
   mid -= 1
   print(input_string[mid:-mid] )
