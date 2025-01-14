def main():
    with open('numbers.txt', 'r') as infile:
        contents = infile.read()
    print(contents)
main()
