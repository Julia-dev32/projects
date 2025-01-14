CONVERT = 0.6214
#always start with def main
def main():
    kilometers = float(input("Enter the distance in kilometers"))
    #need to establish the fuction before use the function
    convert(kilometers)
    #can change the name inside the parenthesis because it will
    # put the value in the same name
def convert(kmeters):
    print(f"miles :{kmeters * CONVERT:.02f}")
main()
