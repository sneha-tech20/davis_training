# Program to find student with highest marks

marks = {"A": 80, "B": 95, "C": 78}

# assume first student has highest marks
top_student = list(marks.keys())[0]

for student in marks:
    if marks[student] > marks[top_student]:
        top_student = student  # update highest

print(top_student)