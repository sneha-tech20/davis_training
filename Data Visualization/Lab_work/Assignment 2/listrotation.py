lst = [10, 20, 30, 40, 50]
k = 2

k = k % len(lst)
rotated = lst[-k:] + lst[:-k]

print(rotated)