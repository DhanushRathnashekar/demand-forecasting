import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

df = pd.read_csv("Data/train.csv", parse_dates=["date"])
daily = df.groupby("date")["sales"].sum().asfreq("D")

train = daily[:"2017-09-30"]
test = daily["2017-10-01":]

# The three forecasts, exactly as in steps 5, 6 and 7
plain_fc = daily.shift(364)["2017-10-01":]
growth = train[-364:].sum() / train[-728:-364].sum()
growth_fc = plain_fc * growth
hw_fc = ExponentialSmoothing(train, trend="add", seasonal="mul", seasonal_periods=7).fit().forecast(len(test))

# Draw the chart
plt.figure(figsize=(12, 5))
plt.plot(test.index, test, label="Actual sales", color="black", linewidth=2)
plt.plot(growth_fc.index, growth_fc, label="Last year + growth (MAPE 1.4%)", linestyle="--")
plt.plot(hw_fc.index, hw_fc, label="Holt-Winters (MAPE 19.2%)", linestyle=":")

# Your turn: add the plain baseline line here
plt.plot(plain_fc.index, plain_fc, label="Same weekday last year (MAPE 4.2%)", linestyle="-.")

plt.title("Daily sales forecast vs actual, October to December 2017")
plt.ylabel("Units sold per day")
plt.legend()
plt.tight_layout()
plt.savefig("chart_forecast_comparison.png")
print("Saved chart_forecast_comparison.png")
