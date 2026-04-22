keyword = input("Enter keyword: ").lower()

with open("file.txt", "r") as f:
    for line in f:
        if keyword in line.lower():
            print(line.strip())