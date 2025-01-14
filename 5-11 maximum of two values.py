def main():
    firstValue = int(input("Enter your first integer: "))
    secondValue = int(input("Enter your second integer: "))
    greaterValue = maxValue(firstValue, secondValue)
    print(f"{greaterValue} is the greatest value")
def maxValue(firstValue, secondValue):
    return max(firstValue, secondValue)
main()
