# Take input for the student that he can attend the exam or not
absent_cause = input("Did you have any issues with the health? (Y/N): ").strip().upper()

# Checking the user input and predicting output accordingly
if absent_cause == 'Y':   # Condition 1
    print("You are allowed")
else:
    # Take input of the attendance
    attendance = int(input("Enter the attendance of the student: "))

    if attendance >= 150:   # Condition 2
        print("Allowed")
    else:
        print("Not allowed")
