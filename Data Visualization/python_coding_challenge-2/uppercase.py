# Program to convert string to uppercase without using upper()

text = input("Enter string: ")
result = ""

for ch in text:
    if 'a' <= ch <= 'z':  # check lowercase
        result += chr(ord(ch) - 32)  # convert to uppercase
    else:
        result += ch

print(result)