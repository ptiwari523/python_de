from utils.transform import transform_orders

sample_data = [
    {"order_id": 1, "amount": "110", "country": "us"},
    {"order_id": 2, "amount": "255", "country": "in"},
]

result = transform_orders(sample_data)

print(result)