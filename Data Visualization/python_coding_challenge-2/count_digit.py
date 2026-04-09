# Program to count number of digits

num = int(input("Enter number: "))
count = 0  # initialize counter

while num > 0:
    count += 1  # increment count
    num //= 10  # remove last digit

print(count)