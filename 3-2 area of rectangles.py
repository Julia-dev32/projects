lengthOfRectangle1 = float(input("Enter the length of rectangle 1"))
widthOfRectangle1 = float(input("Enter width of triangle 1"))
lengthOfRectangle2 = float(input("Eenter the length of rectangle 2"))
widthOfRectangle2 = float(input("Enter the width of rectangle 2"))
areaOfRectangle1 = lengthOfRectangle1 * widthOfRectangle1
areaOfRectangle2 = lengthOfRectangle2 * widthOfRectangle2
if areaOfRectangle1 > areaOfRectangle2: 
    print("Area of triangle 1 is greater")
elif areaOfRectangle2 > areaOfRectangle1:
    print("Area of triangle 2 is greater")
elif areaOfRectangle1 == areaOfRectangle2:
    print("The area of both triangles are the same")
