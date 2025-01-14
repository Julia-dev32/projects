INCHES_PER_FOOT = 12
def main():
    feet = int(input("Enter the amount of feet: "))
    amount_of_inches = feet_to_inches(feet)
    print(f"Feet to inches is : {int(amount_of_inches)}")
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT
main()