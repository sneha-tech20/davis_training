def attendance_tracker(filename):
    data = {}

    with open(filename, 'r') as f:
        next(f)
        for line in f:
            emp_id, date, status = line.strip().split(',')

            if emp_id not in data:
                data[emp_id] = {"present": 0, "total": 0}

            data[emp_id]["total"] += 1
            if status.lower() == "present":
                data[emp_id]["present"] += 1

    low_attendance = []

    for emp, val in data.items():
        percent = (val["present"] / val["total"]) * 100
        if percent < 75:
            low_attendance.append(emp)

    return data, low_attendance