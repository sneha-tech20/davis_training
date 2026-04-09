# Function to return even numbers from list

def get_even(nums):
    result = []
    
    for num in nums:
        if num % 2 == 0:
            result.append(num)
    
    return result

# example
print(get_even([1, 2, 3, 4]))