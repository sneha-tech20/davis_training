# Program to count occurrences of a character

text = input("Enter string: ")
ch = input("Enter character: ")

count = 0

for c in text:
    if c == ch:
        count += 1

print(count)