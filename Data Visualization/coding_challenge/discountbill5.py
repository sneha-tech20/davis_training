price = float(input("Enter price: "))
discount = float(input("Enter discount: "))

price -= (price * discount / 100)

print("Final price after discount:", price)