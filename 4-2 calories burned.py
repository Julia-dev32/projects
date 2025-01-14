caloriesBurned = 0
for minute in range(10, 31, 5):
    caloriesBurned = minute * 4.2
    print(f"in {minute} minutes {caloriesBurned:.0f} calories were burned")

