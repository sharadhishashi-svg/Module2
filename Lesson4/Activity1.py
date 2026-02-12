#Take input of a word
word = input("Please enter your word : ")
#take input of a character
character = input("Please enter a Character : ")
i = 0
count = 0
#loop will to find the occurence of character
while(i < len(word)): #string operation

    if(word[i] == character): #condition 1
        count = count + 1
    i = i + 1

#Display the result
print("The total Number of Times ", character, " has Occurred = " , count)
