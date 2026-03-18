n = int(input("Enter N: "))

numbers = list(range(1, n+1))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:", even_numbers)