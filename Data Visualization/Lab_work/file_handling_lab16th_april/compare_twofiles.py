with open("file1.txt") as f1, open("file2.txt") as f2:
    lines1 = set(f1.readlines())
    lines2 = set(f2.readlines())

diff = lines1 - lines2

print("Lines in file1 but not in file2:")
for line in diff:
    print(line.strip())