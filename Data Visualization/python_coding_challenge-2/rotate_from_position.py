# Program to rotate list by one position (right rotation)

nums = [1, 2, 3]

# move last element to first
last = nums[-1]
nums = [last] + nums[:-1]

print(nums)