P = float(input("Enter Principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))

si = lambda p, r, t: (p * r * t) / 100

print("Simple Interest:", si(P, R, T))