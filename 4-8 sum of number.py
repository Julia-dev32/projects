sum = 0
number = int(input("Enter a number to see sum of numbers"))
while number > 0:
    sum += number
    number = int(input("Enter another number number"))
print(f"Total: {sum}")