orders = [
    {"order_d":1, "country":"US"},
    {"order_d":2, "country":"IN"},
    {"order_d":3, "country":"IN"},
]

in_order = []

for order in orders:
    if order["country"] == 'IN':
        in_order.append(order)

print(in_order)