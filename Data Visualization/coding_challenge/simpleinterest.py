def simple_interest(P, R, T):
    return (P * R * T) / 100

P = float(input("Enter Principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))

SI = simple_interest(P, R, T)
print("Simple Interest:", SI)