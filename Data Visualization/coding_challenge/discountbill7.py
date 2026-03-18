price = float(input("Enter price: "))
discount = float(input("Enter discount: "))

final_price = price * (1 - discount / 100)

print("Final price after discount:", final_price)