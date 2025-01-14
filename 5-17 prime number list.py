def main():
    for number in range(1,101):
        if prime(number):
            print(f"{number} is prime")
        else:
            print(f"{number} is not prime")
        print()
def prime(number):
    if number < 2:
        return False
    half = int(number / 2)
    for count in range(2, half + 1):
        if number % count == 0:
            return False
    return True
main()