def bill_calc(units):
    if units == 0:
        return 0
    if units <= 100:
        return units * 5
    elif units <= 200:
        return 100 * 5 + (units - 100) * 7
    else:
        return 100 * 5 + 100 * 7 + (units - 200) * 10

units = int(input("Enter units: "))
print("Total bill amount:", bill_calc(units))