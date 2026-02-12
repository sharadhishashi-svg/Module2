#take input from user
rows = int(input("enter the number of rows: "))
if rows%2==0: #conditions
  midRow = int(rows/2)
else:
  midRow = int(rows/2)+1
sp = midRow-1
#loop for upper part 
for i in range(1, midRow+1): #loop for rows
  for j in range(1, sp+1): #loop for columns
    print(end=" ")
  sp = sp-1
  num = 1
  for j in range(2*i-1):
    print(end=str(num))
  #incerementing number at each column
    num = num+1
  print()
sp = 1
#loop for lower part
for i in range(1, midRow): #loop for rows
  for j in range(1, sp+1):  #loop for columns
    print(end=" ")
  sp = sp+1
  num = 1
  for j in range(1, 2*(midRow-i)):
    print(end=str(num)) #display result
  #incerementing number at each column
    num = num+1
  print()
