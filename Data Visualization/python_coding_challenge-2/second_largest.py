# Program to find second largest element

nums = [10, 20, 5, 15]

largest = second = float('-inf')  # initialize

for num in nums:
    if num > largest:
        second = largest  # update second
        largest = num     # update largest
    elif num > second and num != largest:
        second = num

print(second)