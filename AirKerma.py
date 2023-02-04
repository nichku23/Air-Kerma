#Air Kerma calculation

mGy_per_min_m = 1
while mGy_per_min_m > 0:
    mGy_per_min_m = float(input("\nWhat is the measured mGy/min (Enter 0 to exit)? "))
    if mGy_per_min_m <= 0:
        break
    mGy_per_min_d = float(input("What is the displayed mGy/min? "))
    mGy_m = float(input("What is the measured mGy? "))
    mGy_d = float(input("What is the displayed mGy? "))
    print("\nAir Kerma = " + str(round((mGy_per_min_m - mGy_per_min_d) / mGy_per_min_m * 100,1)))
    print("Cumulative Air Kerma = " + str(round((mGy_m - mGy_d) / mGy_m * 100,1)))
