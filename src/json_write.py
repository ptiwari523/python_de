import json

data = {
    "orders": [
        {"id": 1, "items":[{"sku":"A1", "qty": 2, "price": 120.0}]},
        {"id": 2, "items":[{"sku":"B2", "qty": 1, "price": 320.0}]},
        {"id": 3, "items":[{"sku":"C1", "qty": 3, "price": 60.50}]},
    ]
}

with open("order.json", "w") as file:
    json.dump(data, file, indent=2)