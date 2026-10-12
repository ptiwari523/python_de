import csv

rows=[
    ["order_id", "name", "amount", "country"],
    [1, "Alice", 120.5, "US"],
    [2, "Bob", 70.5, "IN"],
    [2, "Charlie", 200.0, "US"]
]

with open("orders.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)