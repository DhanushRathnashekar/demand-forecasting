import pandas as pd

df = pd.read_csv("Data/train.csv", parse_dates=["date"])
daily = df.groupby("date")["sales"].sum()

train = daily[:"2017-09-30"]
test = daily["2017-10-01":]

print("Training days:", len(train))
print("Test days:", len(test))
print("Test starts:", test.index.min(), "ends:", test.index.max())
