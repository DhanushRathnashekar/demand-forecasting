import pandas as pd
import numpy as np

df = pd.read_csv("Data/train.csv", parse_dates=["date"])

# One product at one location: store 1, item 1
one = df[(df["store"] == 1) & (df["item"] == 1)]
item = one.set_index("date")["sales"].asfreq("D")

train = item[:"2017-09-30"]
test = item["2017-10-01":]

# Same method as step 6, for this one item
growth = train[-364:].sum() / train[-728:-364].sum()
forecast = item.shift(364)["2017-10-01":] * growth
errors = test - forecast

# Inputs
lead_time = 7.62          # days, from the vendor warehouse project
z = 1.65                  # 95% service level
avg_daily = forecast.mean()
error_sd = errors.std()   # typical size of the daily miss

# Calculation
demand_during_lead = avg_daily * lead_time
safety_stock = z * error_sd * np.sqrt(lead_time)

print("Average forecast per day:", round(avg_daily, 1))
print("Typical daily miss (std):", round(error_sd, 1))
print("Expected demand during lead time:", round(demand_during_lead))
print("Safety stock:", round(safety_stock))

# Your turn: reorder point
reorder_point = demand_during_lead + safety_stock
print("Reorder point:", round(reorder_point))   

print()
print("Sensitivity check: reorder point for different lead times")
for days in [3, 7.62, 14]:
    rp = avg_daily * days + z * error_sd * np.sqrt(days)
    print(days, "days ->", round(rp), "units")