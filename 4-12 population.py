startingNumber = int(input("Enter starting number of population"))
dailyIncrease = int(input("Enter the daily increase"))
daysToMultiply = int(input("Enter number of days to multiply"))
percent = dailyIncrease / 100
population = startingNumber
print(startingNumber)
for number in range(daysToMultiply,1,-1):
    population = population + population * percent
    print(population)
