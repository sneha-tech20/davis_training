# Program to find sum of digits

num = int(input("Enter number: "))
sum_digits = 0  # initialize sum

# loop until number becomes 0
while num > 0:
    sum_digits += num % 10  # add last digit
    num //= 10  # remove last digit

print(sum_digits)