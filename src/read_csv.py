import csv

with open("orders.csv") as file:
    reader = csv.reader(file)
    # for row in reader:
    [print(row) for row in reader]