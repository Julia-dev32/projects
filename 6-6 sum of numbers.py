def main():
    with open('numbers.txt', 'r') as file:
        total = 0
        for line in file:
            total += line
        print(total)
main()