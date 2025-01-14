CLASSA = 20
CLASSB = 15
CLASSC = 10

def main():
    classA = int(input("Enter the amount of tickets bought for class a"))
    classB = int(input("Enter the amount of tickets bought for class B"))
    classc = int(input("Enter the amount of tickets bought for class C"))
    totalCost = (classA * CLASSA) + (classB * CLASSB) + (classc * CLASSC)
    print(totalCost)
main()


