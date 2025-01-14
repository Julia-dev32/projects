
numberOfPackagesBought = int(input("Enter amount of packges bought"))
packageCost = numberOfPackagesBought * 99
if numberOfPackagesBought >= 10 and numberOfPackagesBought <= 19:
    tenPercentDiscount = packageCost * 0.10
    print(tenPercentDiscount)
    print(packageCost - tenPercentDiscount)
elif numberOfPackagesBought >= 20 and numberOfPackagesBought <= 49:
    twentyPercentDiscount = packageCost * 0.20
    print(twentyPercentDiscount)
    print(packageCost - twentyPercentDiscount)
elif numberOfPackagesBought >= 50 and numberOfPackagesBought <= 99:
    thirtyPercentDiscount = packageCost * 0.30
    print(thirtyPercentDiscount)
    print(packageCost - thirtyPercentDiscount)
elif numberOfPackagesBought >= 100:
    fortyPercetnDiscount = packageCost * 0.40
    print(fortyPercetnDiscount)
    print(packageCost - fortyPercetnDiscount)