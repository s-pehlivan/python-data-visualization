import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename="data/sitka_weather_2018_simple.csv"

dates, highs, lows = [], [], []

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)


	for row in reader: 
		high = int(row[5])
		date = datetime.strptime(row[2], "%Y-%m-%d")
		low = int(row[6])

		dates.append(date)
		highs.append(high)
		lows.append(low)


# Plot the highs and lows
plt.style.use("seaborn")
fig, ax = plt.subplots()

ax.plot(dates, highs, c="red", alpha=0.5)
ax.plot(dates, lows, c="blue", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.2)

# Format plot
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()
