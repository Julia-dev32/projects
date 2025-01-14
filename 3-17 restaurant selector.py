#if it has 2 options like yes or no make it boolean true or false
vegetarianresponse = False
veganresponse = False
glutenresponse = False

response = input("Is the party vegetarian")
if response == "yes":
    vegetarianresponse = True

response = input("Is the party vegan?")
if response == "yes":
    veganresponse = True

response = input("Is the party gluten free?")
if response == "yes":
    glutenresponse = True
#not equals true because established that it is false
#listing the "no" response as not

if not veganresponse and not vegetarianresponse and not glutenresponse:
    print("Joes gourmet burger")

if not veganresponse:
    print("Main street Pizza company")

if not veganresponse and not glutenresponse:
    print("Mama's fine Italian")

print("chefs kitchen")
print("corner cafe")