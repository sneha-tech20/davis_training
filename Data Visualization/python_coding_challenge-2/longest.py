# Program to find longest word in a sentence

text = input("Enter sentence: ")
words = text.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print(longest)