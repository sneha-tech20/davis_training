# Program to count frequency of elements

nums = [1, 2, 2, 3]
freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1  # increment count
    else:
        freq[num] = 1   # initialize count

print(freq)