GRAVITY = 9.8
def main():
    for second in range(1,11):
        distance = falling_distance(second)
        print(f"The distance in meters is {distance:.2f}")
        print()
def falling_distance(second):
    return 0.5 * GRAVITY * (second ** 2)
main()