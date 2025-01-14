import random

def main():
    number1 = random.randint(1,100)
    number2 = random.randint(1,100)
    print(f"  {number1}")
    print(f"+ {number2}")
    useranswer = int(input("Enter the sum of these numbers: "))
    realtotal = total(number1, number2)
    answer = answer1(useranswer, realtotal)
def total(number1, number2):
    return (number1 + number2)
def answer1(useranswer, realtotal):
    if realtotal == useranswer:
        print("Congratulations the answer is correct!!")
    else:
        print(f"incorrect the answer is {realtotal}")
main()