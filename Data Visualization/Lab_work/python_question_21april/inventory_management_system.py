import json

inventory = {}

def add_item(name, price, qty):
    inventory[name] = {"price": price, "qty": qty}

def update_item(name, price=None, qty=None):
    if name in inventory:
        if price:
            inventory[name]["price"] = price
        if qty:
            inventory[name]["qty"] = qty

def delete_item(name):
    inventory.pop(name, None)

def save_inventory(file):
    with open(file, 'w') as f:
        json.dump(inventory, f)

def load_inventory(file):
    global inventory
    with open(file, 'r') as f:
        inventory = json.load(f)