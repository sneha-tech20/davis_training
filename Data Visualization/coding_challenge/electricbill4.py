units = int(input("Enter units: "))
bill = 0
i = 1

while i <= units:
    if i <= 100:
        bill += 5
    elif i <= 200:
        bill += 7
    else:
        bill += 10
    i += 1

print("Total bill amount:", bill)