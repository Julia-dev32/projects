def main():
    filename = input("Enter the files name: ")
    userfile = open(filename, "r")


    lineNumber = 0

    for line in userfile:
        lineNumber += 1
        linecontent = userfile.readline()
        print(f"{linecontent} {lineNumber};")

    userfile.close()
main()

