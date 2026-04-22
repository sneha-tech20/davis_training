def group_students(data):
    groups = {}

    for name, grade in data:
        groups.setdefault(grade, []).append(name)

    return groups