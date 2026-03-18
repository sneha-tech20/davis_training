units = int(input("Enter units: "))

rates = { "first": 5, "second": 7, "third": 10 }

if units <= 100:
    bill = units * rates["first"]
elif units <= 200:
    bill = 100 * rates["first"] + (units - 100) * rates["second"]
else:
    bill = 100 * rates["first"] + 100 * rates["second"] + (units - 200) * rates["third"]

print("Total bill amount:", bill)