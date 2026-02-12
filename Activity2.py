# Take input of number of units consumed from the user
num_of_units = int(input(" Please enter Number of Units you Consumed : "))

# Check conditions of units consumed 
# Then calculate amount and surcharge accordingly
# surcharge is the tax value

# Check for units less than 50
if(num_of_units < 50):
    amount = num_of_units * 5.74
    surcharge = 30 

# Check for units less than 100
elif(num_of_units <= 100):
    amount = 120 + ((num_of_units - 50) * 6.21)
    surcharge =40

# Check for units less than or equal to 200
elif(num_of_units <= 200):
    amount = 120 + 162.50 + ((num_of_units - 100) * 6.74)
    surcharge =50

# Check for all the cases other than mentioned 
# When units consumed are more than 200
else:
    amount = 120 + 162.50 + 526 + ((num_of_units - 200) * 7.45)
    surcharge =60

# Calculate and Display the total electricity bill
# total amount = amount + surcharge
total = amount + surcharge
print("\nElectricity Bill = %.2f"  %total)