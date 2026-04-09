# Program to find duplicate characters

text = input("Enter string: ")
seen = []
duplicates = []

for ch in text:
    if ch not in seen:
        seen.append(ch)  # store first occurrence
    elif ch not in duplicates:
        duplicates.append(ch)  # store duplicate

print(" ".join(duplicates))