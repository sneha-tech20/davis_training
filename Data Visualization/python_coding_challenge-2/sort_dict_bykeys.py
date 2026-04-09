# Program to sort dictionary by keys

data = {"b": 2, "a": 1}

# sort keys and rebuild dictionary
sorted_dict = {}

for key in sorted(data):
    sorted_dict[key] = data[key]

print(sorted_dict)