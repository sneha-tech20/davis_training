# Program to find maximum without using max()

nums = [5, 8, 2]

max_val = nums[0]  # assume first element is largest

# compare each element
for num in nums:
    if num > max_val:
        max_val = num  # update max

print(max_val)