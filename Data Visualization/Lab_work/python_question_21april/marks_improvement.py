def load_marks(file):
    data = {}
    with open(file, 'r') as f:
        for line in f:
            name, marks = line.strip().split(',')
            data[name] = float(marks)
    return data

def improvement(old_file, new_file):
    old = load_marks(old_file)
    new = load_marks(new_file)

    improved = {}

    for student in new:
        if student in old and new[student] > old[student]:
            diff = new[student] - old[student]
            percent = (diff / old[student]) * 100
            improved[student] = percent

    return improved