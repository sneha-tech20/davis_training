price = float(input("Enter price: "))
discount = float(input("Enter discount percentage: "))

final_price = price - (price * discount / 100)

print("Final price after discount is:", final_price)