total = 0
count = 1
while count < 6:
    bugcollected = int(input("Enter amount of bugs collected on this day"))
    count += 1
    total += bugcollected
    #have to assign a number to total to be able to add to it
print(total)