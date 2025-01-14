STATETAX = 0.05
COUNTYTAX = 0.025
def main():
    totalsales = float(input("Enter total sales this month"))
    countysalestax = countysales(totalsales)
    statesalestax = statesales(totalsales)
    totalsalestax = countysalestax + statesalestax
    print(f"The county sales tax this month is : ${countysalestax:.2f}")
    print(f"The state sales tax this month is : ${statesalestax:.2f}")
    print(f"The total sales tax is : ${totalsalestax:.2f}")
def countysales(totalsales):
    return totalsales * COUNTYTAX
def statesales(totalsales):
    return totalsales * STATETAX
main()



