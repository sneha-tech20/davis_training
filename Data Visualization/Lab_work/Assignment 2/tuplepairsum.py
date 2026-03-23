t = (1, 2, 3, 4, 5)
target = 5
pairs = []

for i in range(len(t)):
    for j in range(i+1, len(t)):
        if t[i] + t[j] == target:
            pairs.append((t[i], t[j]))

print(pairs)