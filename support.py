
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

dataframe = pd.read_csv('EURAUD240.csv', names=["Date", "Time", "Open", "High", "Low", "Close", "Volume"])
close = dataframe["Close"]
# close = np.asarray(close)
# print(close)
High = dataframe["High"]
Low = dataframe["Low"]
Close = dataframe["Close"]

High = np.max(High)
Low = np.min(Low)
Close = Close[len(Close)-1]
# Close = Close[:-1]
print("High: {0}".format(High))
print("Low: {0}".format(Low))
print("Close: {0}".format(Close))

# 1.Support(S)= (Pivot*2)-High

# 2.Resistance(R)=(Pivot*2)-Low

pp = (High + Low + Close) / 3
r1 = (2 * pp) - Low
s1 = (2 * pp) - High

# r2 = pp + (High - Low)
# s2 = pp - (High - Low)

# r3 = High + 2 * (pp - Low)
# s3 = Low - 2 * (High - pp)

print(type(close))
print("pp: {0}".format(pp))
print("r1: {0}, s1: {1}".format(r1, s1))
# print("r2: {0}, s2: {1}".format(r2, s2))
# print("r3: {0}, s3: {1}".format(r3, s3))
# support, resistance = supress(close, len(close) - 1)
# print(support, resistance)
plt.plot(close, 'b')
# plt.plot()
plt.axhline(y=r1, color='r', linestyle='-', label='800 Similarity')
# plt.axhline(y=r2, color='r', linestyle='-')
# plt.axhline(y=r3, color='r', linestyle='-')
plt.axhline(y=s1, color='g', linestyle='-')
plt.axhline(y=pp, color='y', linestyle='-')
# plt.axhline(y=s2, color='g', linestyle='-')
# plt.axhline(y=s3, color='g', linestyle='-')
plt.title('EURAUD240')
plt.ylabel('Price')
plt.show()
