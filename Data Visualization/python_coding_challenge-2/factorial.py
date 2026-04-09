# Program to calculate factorial of a number

n = int(input("Enter number: "))
fact = 1  # initialize factorial

# loop from 1 to n
for i in range(1, n + 1):
    fact *= i  # multiply each number

print(fact)