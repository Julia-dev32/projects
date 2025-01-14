def main():
    loanPayment = float(input("Enter loan payment:"))
    insurance = float(input("Enter insurance cost:"))
    gas = float(input("Enter gas cost:"))
    oil = float(input("Enter oil cost"))
    tires = float(input("Enter tire cost:"))
    maintenance = float(input("Enter maintenance cost:"))
    totalCostsMonthly(loanPayment, insurance, gas, oil, tires, maintenance)
def totalCostsMonthly(loanPayment, insuarance, gas, oil, tires, maintenance):
    totalCostMonthly = loanPayment + insuarance + gas + oil + tires + maintenance
    print(f"Total monthly costs is ${totalCostMonthly:.2f}")
    totalAnnually(totalCostsMonthly)
def totalAnnually(totalCostsMonthly):
    annualCost = totalCostsMonthly * 12
    print(f"The annual cost is ${annualCost:.2f}")
main()


