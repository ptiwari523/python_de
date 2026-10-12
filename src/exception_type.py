price= "100"
try:
    amount = price
    total = amount + 50
except TypeError:
    amount = int(price)
    total = amount + 50
    print(total)
