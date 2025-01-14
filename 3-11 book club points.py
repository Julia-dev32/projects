numberOfBooksPurchased = int(input("Enter amount of books purchased"))
if numberOfBooksPurchased == 0:
    print("Earned 0 points")
elif numberOfBooksPurchased >= 2 and numberOfBooksPurchased < 4:
    print("Earned 5 points")
elif numberOfBooksPurchased >= 4 and numberOfBooksPurchased < 6:
    print("Earned 15 points")
elif numberOfBooksPurchased >= 6 and numberOfBooksPurchased < 8:
    print("Earned 30 points")
elif numberOfBooksPurchased >= 8:
    print("Earned 60 points")
