totalsalary = 0
salary = 1
numberOfDays = int(input('Enter number of days'))
while numberOfDays > 0:
    totalsalary += salary
    salary += salary
    print(f"{salary} pennies")
    numberOfDays -= 1
print(f"Total: ${totalsalary / 100}")
