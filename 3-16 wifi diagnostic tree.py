print("Reboot the computer and try to connect")
fix1 = input("Did that fix the problem. Yes or No")
if fix1 == "No":
    print("Reboot the router and try to connect")
    fix2 = input("Did that fix the problem. Yes or No")
    if fix2 == "No":
        print("Make sure the cables between the router and modem are plugged in firmly")
        fix3 = input("Did that fix the problem. Yes or No")
        if fix3 == "No":
            print("Move the router to a new location and try to connect")
            fix4 = input("Did that fix the problem. Yes or No")
            if fix4 == "No":
                print("Get a new router")