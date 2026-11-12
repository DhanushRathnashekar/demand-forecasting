import pandas as pd

df = pd.read_csv("Data/train.csv", parse_dates=["date"])

print(df.head())
print()
print("Rows and columns:", df.shape)
print("First date:", df["date"].min())
print("Last date:", df["date"].max())
print("Stores:", df["store"].nunique())
print("Items:", df["item"].nunique())
print("Total units sold:", df["sales"].sum())
