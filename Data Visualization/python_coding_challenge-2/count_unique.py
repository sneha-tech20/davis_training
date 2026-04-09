# Program to count unique elements

nums = [1, 1, 2, 3, 3]

unique = []

# add only unique values
for num in nums:
    if num not in unique:
        unique.append(num)

print(len(unique))