import string

freq = {}

with open("article.txt", "r") as f:
    for line in f:
        line = line.lower().translate(str.maketrans("", "", string.punctuation))
        words = line.split()
        for word in words:
            freq[word] = freq.get(word, 0) + 1

for word, count in freq.items():
    print(word, ":", count)