# Program to find missing number in sequence

nums = [1, 2, 4, 5]

n = len(nums) + 1  # total numbers including missing

# sum of first n natural numbers
total = n * (n + 1) // 2

# subtract actual sum
missing = total - sum(nums)

print(missing)