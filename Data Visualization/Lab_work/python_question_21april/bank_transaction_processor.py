def process_transactions(file):
    balances = {}

    with open(file, 'r') as f:
        for line in f:
            acc, typ, amt = line.strip().split(',')
            amt = float(amt)

            balances.setdefault(acc, 0)

            if typ == "deposit":
                balances[acc] += amt
            elif typ == "withdraw":
                if balances[acc] < amt:
                    raise ValueError(f"Overdraft for {acc}")
                balances[acc] -= amt

    return balances