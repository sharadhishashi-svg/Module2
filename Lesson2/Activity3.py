# input number greater than 1
number = int(input("Enter the number: "))

# print the numbers from n to 1
print ("numbers from {0} to {1} are: ".format(number,1))

# loop to print numbers 
for i in range(number,0,-1):
	print (i)