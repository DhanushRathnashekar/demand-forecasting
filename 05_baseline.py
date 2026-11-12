import pandas as pd

df = pd.read_csv("Data/train.csv", parse_dates=["date"])
daily = df.groupby("date")["sales"].sum()

train = daily[:"2017-09-30"]
test = daily["2017-10-01":]

# Baseline: same weekday 52 weeks (364 days) earlier
forecast = daily.shift(364)["2017-10-01":]

errors = test - forecast
mae = errors.abs().mean()

print("Average daily sales in test period:", round(test.mean()))
print("MAE (average miss, units per day):", round(mae))
print("Average error (positive = forecast too low):", round(errors.mean()))

# Your turn: MAPE
mape = (errors.abs() / test).mean() * 100
print("MAPE (average miss, %):", round(mape, 1))