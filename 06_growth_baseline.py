import pandas as pd

df = pd.read_csv("Data/train.csv", parse_dates=["date"])
daily = df.groupby("date")["sales"].sum()

train = daily[:"2017-09-30"]
test = daily["2017-10-01":]

# Growth: last 52 weeks of training vs the 52 weeks before that
recent_year = train[-364:].sum()
previous_year = train[-728:-364].sum()
growth = recent_year / previous_year
print("Growth factor:", round(growth, 3))

# Forecast: same weekday last year, multiplied by growth
forecast = daily.shift(364)["2017-10-01":] * growth

errors = test - forecast
mae = errors.abs().mean()
print("MAE (average miss, units per day):", round(mae))
print("Average error (positive = forecast too low):", round(errors.mean()))

# Your turn: MAPE (same two lines as last time)
mape = (errors.abs() / test).mean() * 100
print("MAPE (average miss, %):", round(mape, 1))
