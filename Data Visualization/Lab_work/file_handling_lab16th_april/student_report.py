with open("students.txt", "r") as f, open("top_students.txt", "w") as out:
    for line in f:
        name, marks, city = line.strip().split(",")
        if int(marks) > 75:
            out.write(line)

print("Filtered students saved.")