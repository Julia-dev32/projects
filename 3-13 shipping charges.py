weightOfPackage = int(input("Enter weight of package"))
if weightOfPackage <= 2:
    print("Shipping charges = " + str(weightOfPackage * 1.50))
elif weightOfPackage > 2 and weightOfPackage <= 6:
    print("Shipping charges = " + str(weightOfPackage * 3))
elif weightOfPackage > 6 and weightOfPackage <= 10:
    print("Shipping charges = " + str(weightOfPackage * 4))
elif weightOfPackage > 10:
    print("Shipping charges = " + str(weightOfPackage * 4.75))
