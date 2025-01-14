def main():
    presentValue = float(input("Enter the accounts present value: "))
    monthlyIntrestRate = float(input("Enter the monthly intrest rate: "))
    numberOfMonths = int(input("Enter the total number of months: "))
    futureValue = futurev(presentValue, monthlyIntrestRate, numberOfMonths)
    print(f"The future value is ${futureValue:.2f}")
def futurev(p, i, t):
    return p * (1 + i) ** t
main()
