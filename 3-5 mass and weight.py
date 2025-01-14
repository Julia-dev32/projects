objectMass = float(input("Enter onjects mass"))
weight = objectMass * 9.8
if weight > 500:
    print("Object is too heavy")
elif weight < 100:
    print("Object is too light")