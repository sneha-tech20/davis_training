# Bonus Calculation Program

salary = float(input("Enter salary: "))

if salary <= 50000:
    bonus = salary * 0.07
else:
    bonus = salary * 0.10

print("Bonus =", int(bonus))