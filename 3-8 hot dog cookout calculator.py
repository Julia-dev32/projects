hotDogs = 10
hotDogBuns = 8
peopleAttending = int(input("Enter amount of people going to cookout"))
amountOfHotDogsGivenPerPerson = int(input("Enter amount of hotdogs given per person"))
numberOfHotDogsRequired = peopleAttending * amountOfHotDogsGivenPerPerson
numberOfHotDogBunsRequired = numberOfHotDogsRequired
numberOfPackagesHotdogsrequired = numberOfHotDogsRequired // 10
leftoverhotdogs = numberOfHotDogsRequired % 10
numberOfPackagesHotDogBuns = numberOfHotDogBunsRequired // 8
leftoverhotdogbuns = numberOfHotDogBunsRequired % 8
print(numberOfPackagesHotdogsrequired)
print(numberOfPackagesHotDogBuns)
print(leftoverhotdogbuns)
print(leftoverhotdogs)