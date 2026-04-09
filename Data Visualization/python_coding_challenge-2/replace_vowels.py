# Program to replace vowels with '*'

text = input("Enter string: ")
result = ""

for ch in text:
    if ch.lower() in "aeiou":
        result += "*"  # replace vowel
    else:
        result += ch

print(result)