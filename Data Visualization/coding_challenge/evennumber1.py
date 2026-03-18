n = int(input("Enter N: "))
even_list = []

for i in range(1, n + 1):
    if i % 2 == 0:
        even_list.append(i)

print("Even numbers:", even_list)