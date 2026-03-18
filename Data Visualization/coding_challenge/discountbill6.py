price, d = map(float, input("Enter price and discount: ").split())

final = price * ((100 - d) / 100)

print("Final price:", final)