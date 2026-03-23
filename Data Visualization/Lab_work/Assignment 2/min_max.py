t = (5, 1, 8, 3)

max_val = t[0]
min_val = t[0]

for i in t:
    if i > max_val:
        max_val = i
    if i < min_val:
        min_val = i

print("Max =", max_val, "Min =", min_val)