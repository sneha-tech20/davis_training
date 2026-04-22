seen = set()
error_count = 0

with open("log.txt") as f:
    for line in f:
        if "ERROR" in line and line not in seen:
            print(line.strip())
            seen.add(line)
            error_count += 1

print("Total ERROR logs:", error_count)