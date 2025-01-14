number = int(input("Enter a positive number"))
factorial = 1
if number > 0:
    for numb in range(number,0,-1):
        factorial = factorial * numb
print(factorial)
    