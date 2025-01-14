month = int(input("Enter the month in numeric form"))
day = int(input("Enter the day"))
year = int(input("Enter the year with 2 digits"))
if month * day == year:
    print("magic date")
else:
    print("not magic date")