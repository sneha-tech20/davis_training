# Program to check if two strings are anagrams

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# compare sorted strings
if sorted(s1) == sorted(s2):
    print(True)
else:
    print(False)