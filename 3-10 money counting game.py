
amountOfPennies = int(input("Enter number of pennies"))
amountOfQuarters = int(input("Enter number of quarters"))
amountOfNickels = int(input("Enter number of nikckels"))
amountOfDimes = int(input("Enter number of dimes"))
totalAmount = amountOfDimes * 0.10 + amountOfNickels * 0.05 + amountOfPennies * 0.01 + amountOfQuarters * 0.25
if totalAmount == 1.00:
    print("Congrats you won!")
elif totalAmount < 1.00:
    print("Your amount was less then a dollar")
elif totalAmount > 1.00:
    print("Your amount was more then one dollar")