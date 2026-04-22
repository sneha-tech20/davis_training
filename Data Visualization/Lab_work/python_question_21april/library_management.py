import json

library = {}

def add_book(name):
    library[name] = {"available": True}

def issue_book(name):
    if library.get(name, {}).get("available"):
        library[name]["available"] = False
    else:
        print("Not available")

def return_book(name):
    if name in library:
        library[name]["available"] = True

def save(file):
    with open(file, 'w') as f:
        json.dump(library, f)

def load(file):
    global library
    with open(file, 'r') as f:
        library = json.load(f)