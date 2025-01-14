speedmph = int(input("what is the speed in mph"))
hours = int(input("how much hours has it traveled"))
while hours >= 1:
    print(f"{hours} hours {hours * speedmph} miles")
    hours -= 1