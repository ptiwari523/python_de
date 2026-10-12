import json

with open("order.json") as file:
    data = json.load(file)

    rows= []

    for order in data["orders"]:
        for item in order["items"]:
            rows.append({
                "order_id": order["id"],
                "sku": item["sku"],
                "qty": item["qty"],
                "price": item["price"]
            })

    for row in rows:
        print(row)

