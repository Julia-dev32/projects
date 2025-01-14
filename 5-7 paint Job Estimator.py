def main():
    squareFeet = int(input('Enter the square feet'))
    pricePerGallon = float(input('Enter price of paint per gallon'))
    hoursNeeded = hours(squareFeet)
    costOfLabor = laborCost(hoursNeeded)
    gallonsRequired = gallons(squareFeet)
    costOfPaint = paintCost(pricePerGallon, gallonsRequired)
    totalCost = (costOfLabor + costOfPaint)
    print(f"Hours of labor needed is {hoursNeeded:.1f}")
    print()
    print(f"The cost of labor is ${costOfLabor:.2f}")
    print()
    print(f"The amount of gallons required is {int(gallonsRequired)}")
    print()
    print(f"The cost of paint is ${costOfPaint:.2f}")
    print()
    print(f"The total cost is ${totalCost:.2f}")
def hours(squareFeet):
    return (squareFeet / 112) * 8
def laborCost(hoursNeeded):
    return 35 * hoursNeeded
def gallons(squareFeet):
    gallonsOfPaintRequired = squareFeet // 112
    if squareFeet % 112 >= 1:
        gallonsOfPaintRequired += 1
    return gallonsOfPaintRequired
def paintCost(pricePerGallon, gallonsRequired):
    return pricePerGallon * gallonsRequired
main()