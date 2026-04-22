from collections import deque

n = int(input("Enter number of lines: "))

with open("file.txt", "r") as f:
    last_lines = deque(f, maxlen=n)

for line in last_lines:
    print(line.strip())