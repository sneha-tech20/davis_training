def SI(p, r, t):
    if t == 0:
        return 0
    return (p * r / 100) + SI(p, r, t-1)

p, r, t = map(float, input("Enter P R T: ").split())

print("Simple Interest:", SI(p, r, int(t)))