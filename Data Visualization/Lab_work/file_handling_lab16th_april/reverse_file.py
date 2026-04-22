with open("input.txt", "r") as f:
    lines = f.readlines()

with open("reversed.txt", "w") as out:
    for line in reversed(lines):
        out.write(line)

print("File reversed.")

