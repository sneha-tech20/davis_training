# Program to find common elements between two lists

list1 = [1, 2, 3]
list2 = [2, 3, 4]

common = []

# check each element of list1 in list2
for num in list1:
    if num in list2:
        common.append(num)

print(common)