# Program to count words in a sentence

text = input("Enter sentence: ")

words = text.split()  # split into words
print(len(words))     # count words