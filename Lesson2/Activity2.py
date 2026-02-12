#Input a word or sentence
word = input("Please enter your any word : ")

reverse = ('')
#loop for printing in reverse 
for i in word:
    reverse = i + reverse
    
print("\nThe Original String = ", word)
print("The Reversed String = ", reverse)
