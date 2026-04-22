longest = ""

with open("file.txt", "r") as f:
    for line in f:
        if len(line) > len(longest):
            longest = line

print("Longest line length:", len(longest))
print("Content:", longest)