def grade(p):
    if p >= 90: return "A"
    elif p >= 75: return "B"
    elif p >= 50: return "C"
    else: return "F"

toppers = []
max_percent = 0

with open("students.txt") as f:
    for line in f:
        try:
            id_, name, m1, m2, m3 = line.strip().split(",")
            m1, m2, m3 = int(m1), int(m2), int(m3)

            total = m1 + m2 + m3
            percent = total / 3
            g = grade(percent)

            print(name, total, percent, g)

            if percent > max_percent:
                toppers = [name]
                max_percent = percent
            elif percent == max_percent:
                toppers.append(name)

        except:
            print("Invalid record skipped")

print("Topper(s):", toppers)