#Take input from user
n = int(input("Please Enter the total Number of Rows  : "))
count = 1 #initialise by 1

print("Floyd's Triangle") 
#outer loop for number of rows
for i in range(1, n + 1):
  #inner loop for number of columns
    for j in range(1, i + 1):   
      #display result     
        print(count, end = '  ')
        count = count + 1
    print()