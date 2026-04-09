# Program to remove spaces from string

text = input("Enter string: ")
result = ""

for ch in text:
    if ch != " ":  # skip spaces
        result += ch

print(result)