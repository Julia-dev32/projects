INSURSNCE = 0.8
def main():
    replacementCost = float(input("Enter replacement cost of the building:"))
    calculate_insurance(replacementCost)
def calculate_insurance(replacementCost):
    minimum = replacementCost * INSURSNCE
    print(f"Minimum amount of insurance you will pay is {minimum}")
main()

