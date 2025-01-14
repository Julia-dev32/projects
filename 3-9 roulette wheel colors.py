pocketNumber = int(input("Enter pocket number between 0 and 36"))
if pocketNumber == 0:
    print("green")
    #By using and, you're ensuring that you're only checking for numbers that
    #actually fall within the specified range.
elif pocketNumber >= 1 and pocketNumber <= 10:
    if pocketNumber % 2 == 0:
        print("black")
    else:
        print("red")
elif pocketNumber >= 11 and pocketNumber <= 18:
    if pocketNumber % 2 == 0:
        print("red")
    else:
        print("black")
elif pocketNumber >= 19 and pocketNumber <= 28:
    if pocketNumber % 2 == 0:
        print("black")
    else: 
        print("red")
elif pocketNumber >= 29 and pocketNumber <= 36:
    if pocketNumber % 2 == 0:
        print("red")
    else:
        print("black")
else:
    print("Error number is outside of range 0 through 36")
