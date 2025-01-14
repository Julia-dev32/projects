ASSESMENTVALUE = 0.6
PROPERTYTAX = 0.0072

def main():
    valueOfProperty = float(input("Enter actual value of property: "))
    assesmentValue(valueOfProperty)
def assesmentValue(valueOfProperty):
    actualAssesmentValue = valueOfProperty * ASSESMENTVALUE
    print(f"The actual assesment value is ${actualAssesmentValue:.2f}")
    propertyTax(actualAssesmentValue)
def propertyTax(actualAssesmentValue):
    amountPorpertyTax = actualAssesmentValue * PROPERTYTAX
    print(f"The property tax is ${amountPorpertyTax:.2f}")
main()


