rise = 0
thisYear = 0
for year in range(1,26,1):
    rise += 1.6
    thisYear += 1
    print(f"ocean has risen {rise:.01f} mm in year {thisYear}")