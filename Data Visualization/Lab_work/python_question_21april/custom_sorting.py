def custom_sort(data):
    n = len(data)

    for i in range(n):
        for j in range(n - i - 1):
            if (data[j][1] < data[j+1][1]) or \
               (data[j][1] == data[j+1][1] and data[j][2] > data[j+1][2]):
                data[j], data[j+1] = data[j+1], data[j]

    return data