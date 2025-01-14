def main():
    file = open('names.txt', 'r')
    count = 0 
    for line in file:
        count += 1
    file.close
    print(count)
if __name__ == "__main__":      
    main()