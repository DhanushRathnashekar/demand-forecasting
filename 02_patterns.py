import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/train.csv", parse_dates=["date"])

daily = df.groupby("date")["sales"].sum()

daily.plot(figsize=(12, 4), title="Total daily sales, all stores and items")
plt.ylabel("Units sold")
plt.tight_layout()
plt.savefig("chart_daily_sales.png")
print("Saved chart_daily_sales.png")
