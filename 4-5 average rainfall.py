totalInches = 0
totalmonths = 0
years = int(input("Enter the number of years"))
while years > 0:
    for months in range(1,13,1):
        print(f'month {months}')
        rainfallInches = int(input("Enter amount of rain this month in inches"))
        totalInches += rainfallInches
        totalmonths += 1
    years -= 1
    if years == 0:
        break
averagerain = totalInches / totalmonths
print(f'Total inches of rain: {totalInches}')
print(f"Total months: {totalmonths}")
print(f"Average inches of rain per month: {averagerain:.01f}")