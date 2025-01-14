seconds = int(input("Enter number of seconds"))
if seconds >= 86400:
    days = seconds // 86400
    remainderseconds = seconds % 86400
    hours = remainderseconds // 3600
    remainderseconds %= 3600
    minutes = remainderseconds // 60
    seconds = remainderseconds % 60
    print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
elif seconds >= 3600:
    hours = seconds //3600
    remainderseconds = seconds % 3600
    minutes = remainderseconds // 60
    seconds = remainderseconds % 60
    print(f"{hours} hours, {minutes} minutes, {seconds} seconds")
elif seconds >= 60:
    minutes = seconds // 60
    seconds = seconds % 60
    print(f"{minutes} minutes, {seconds} seconds")
else:
    print(f"{seconds} seconds")