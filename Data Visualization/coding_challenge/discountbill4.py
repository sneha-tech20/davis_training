price = float(input("Enter price: "))
discount = float(input("Enter discount: "))

final = lambda p, d: p - (p * d / 100)

print("Final price after discount:", final(price, discount))