import random

def main():
    total_numbers = 0
    while total_numbers < 100:
        number = random.randint(1,100)
        if number % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")
        total_numbers += 1
main()