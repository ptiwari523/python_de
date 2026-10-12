def calculate_total(order):
    if "amount" not in order:
        raise ValueError("Missing 'amount' field!")
    return order["amount"] * 2

order = {"amout": 100}

print(calculate_total(order))