#Input a number 
number = int(input("Enter the number : "))
temp = number
numLen = 0
#iterate the loop
while temp>0: 
  numLen = numLen+1
  temp = int(temp/10)

if numLen>=4: #condition 1
  numLen = int(numLen/2)
  check = 0
  while number>0: #iterate loop
    remainder = number%10
    if check==numLen: #nested condition 1
      midOne = remainder
    elif check==(numLen-1): 
      midTwo = remainder
    number = int(number/10)
    check = check+1
  product = midOne*midTwo #product of middle digits
  #display the result
  print("\nProduct of Mid digits (" +str(midOne)+ "*" +str(midTwo)+ ") = ", product)

else:
  print("\nIt's not a 4 or more than 4-digit number!")