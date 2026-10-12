import pandas as pd

df = pd.read_csv("data/raw/messy_orders.csv")
print(df)

df["amount"] = df["amount"].fillna(0)

df["amount"] = df["amount"].astype(int)

df["country"] = df["country"].str.lower()

print(df)

country_summary = (
    df.groupby("country")
    .agg(
        total_order = ("order_id", "count"),
        total_amount = ("amount", "sum")
    )
)

print(country_summary)

df["running_sum"] = df["amount"].cumsum()

print(df)