n = int(input("Enter N: "))
i = 1
even = []

while i <= n:
    if not i % 2:
        even.append(i)
    i += 1

print(even)