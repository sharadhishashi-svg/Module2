#Input the value of terms
natural_number = int(input("Enter the number: "))

sum = 0  #initialise
x = 1  #initialise
while x<=natural_number: #loop will run from 1 to n
  sum = sum+x
  x = x+1

print("\nSum of natural numbers =", sum)