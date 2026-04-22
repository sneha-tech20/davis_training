transactions = [
    ("user1", 5000),
    ("user1", 7000),
    ("user2", 200),
]

threshold = 4000
flagged = {}

for user, amount in transactions:
    if amount > threshold:
        flagged.setdefault(user, []).append(amount)

print("Suspicious:", flagged)