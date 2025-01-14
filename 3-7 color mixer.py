
firstColor = input("Enter first primary color in lower case")
secondColor = input("Enter second primary color in lower case")
if firstColor == "red" and secondColor == "blue":
    print("purple")
elif firstColor == "blue" and secondColor == "red":
    print("purple")
elif firstColor == "red" and secondColor == "yellow":
    print("orange")
elif firstColor == "yellow" and secondColor == "red":
    print("orange")
elif firstColor == "blue" and secondColor == "yellow":
    print("green")
elif firstColor == "yellow" and secondColor == "blue":
    print("green")
else:
    print("Error")
