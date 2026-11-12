import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

df = pd.read_csv("Data/train.csv", parse_dates=["date"])
daily = df.groupby("date")["sales"].sum().asfreq("D")

train = daily[:"2017-09-30"]
test = daily["2017-10-01":]

model = ExponentialSmoothing(train, trend="add", seasonal="mul", seasonal_periods=7).fit()
forecast = model.forecast(len(test))

errors = test - forecast
print("MAE (average miss, units per day):", round(errors.abs().mean()))
print("Average error (positive = forecast too low):", round(errors.mean()))

# Your turn: MAPE
mape = (errors.abs() / test).mean() * 100
print("MAPE (average miss, %):", round(mape, 1))    
