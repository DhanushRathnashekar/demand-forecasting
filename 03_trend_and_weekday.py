import pandas as pd

df = pd.read_csv("Data/train.csv", parse_dates=["date"])

# Part 1: total sales per year (checks the trend)
df["year"] = df["date"].dt.year
print("Total sales per year:")
print(df.groupby("year")["sales"].sum())
print()

# Part 2: average sales per weekday (checks the weekly pattern)
df["weekday"] = df["date"].dt.day_name()
print("Average sales per weekday:")
print(df.groupby("weekday")["sales"].mean().sort_values(ascending=False))