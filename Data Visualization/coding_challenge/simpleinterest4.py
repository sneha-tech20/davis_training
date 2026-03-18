def SI(p, r, t):
    return (p * r * t) // 100   # using integer division

p = int(input("Enter P: "))
r = int(input("Enter R: "))
t = int(input("Enter T: "))

print("Simple Interest:", SI(p, r, t))