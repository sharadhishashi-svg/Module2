#input an integer value 
num = int(input("Enter the number whose sum you want to find: "))
sum_of_num=0

#Iterates for n+1 times: i=1 to n+1
for i in range(1, num+1): 
  sum_of_num = sum_of_num+i
  print("\nSum of the number =", sum_of_num)
