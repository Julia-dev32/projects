tuition = 8000
years = 0
for year in range(1,6,1):
    tuitionincrease = tuition * 0.03
    tuition = tuition + tuitionincrease
    years += 1
    print(f"tuition in year {years} is ${tuition:.02f}")