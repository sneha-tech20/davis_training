with open("file1.txt") as f1, open("file2.txt") as f2, open("merged.txt", "w") as out:
    line_num = 1
    for line in f1:
        out.write(f"{line_num}. {line}")
        line_num += 1
    for line in f2:
        out.write(f"{line_num}. {line}")
        line_num += 1

print("Files merged.")