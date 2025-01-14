import random
def main():
    while True:
        randomNumber = randomnum()
        while True:
            usernumber = int(input("Guess a number 1-100: "))
            userguess = rightorwrong(usernumber, randomNumber)
            if usernumber == randomNumber:
                break
def randomnum():
    return random.randint(1,100)
def rightorwrong(usernumber, randomNumber):
    if usernumber == randomNumber:
        print(f"Conratulaions you were right")
    elif usernumber > randomNumber:
        print("Too high, try again")
    elif usernumber < randomNumber:
        print("Too low, try again")
main()