# Function to calculate total bill amount

def total_bill(items):
    total = 0
    
    for price in items:
        total += price  # add each item
    
    return total

# example
print(total_bill([100, 200, 300]))