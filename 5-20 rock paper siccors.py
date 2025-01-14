import random

def main():
    while True:
        computerAnswer = random.randint(1,3)
        useranswer = input("Enter rock, paper, or scissors: ")
        useranswertranslated = translated(useranswer)
        computerstring = string(computerAnswer)
        print(f"The computer answer is {computerstring}")
        winner = win(computerAnswer, useranswertranslated)
        print()
def translated(useranswer):
    if useranswer == "paper":
        return 1
    elif useranswer == "rock":
        return 2
    elif useranswer == "scissors":
        return 3
def string(computerAnswer):
    if computerAnswer == 1:
        return "paper"
    elif computerAnswer == 2:
        return "rock"
    elif computerAnswer == 3:
        return "scissors"
def win(computerAnswer, useranswertranslated):
    if computerAnswer == 2 and useranswertranslated == 3:
        print("You lost, try again")
    elif computerAnswer == 3 and useranswertranslated == 2:
        print("Congrats you won")
    elif computerAnswer == 1 and useranswertranslated == 2:
        print("You lost, try again")
    elif computerAnswer == 2 and useranswertranslated == 1:
        print("Congrats you won")
    elif computerAnswer == 1 and useranswertranslated == 3:
        print("Congrats you won")
    elif computerAnswer == 3 and useranswertranslated == 1:
        print("You lost, try again")
    elif computerAnswer == useranswertranslated:
        print("Tie, try again")
main()
