#take two input from user
small = int(input("enter a lower range: "))
high = int(input("enter a upper range: "))

print("Prime numbers between", small, "and", high, "are:")
#iterate loop from lower limit to upper limit
for number in range(small, high + 1):
   # all prime numbers are greater than 1
   if number > 1:
       for i in range(2, number):
           if (number % i) == 0:
               break
       else:
           print(number)