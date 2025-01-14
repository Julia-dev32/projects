def main():
    filename = input("Enter files name: ")
    userfile = open(filename, "r")

    line1 = userfile.readline()
    line2 = userfile.readline()
    line3 = userfile.readline()
    line4 = userfile.readline()
    line5 = userfile.readline()


    userfile.close()

    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
main()