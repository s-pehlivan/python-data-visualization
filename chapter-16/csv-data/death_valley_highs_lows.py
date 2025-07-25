import csv 
from datetime import datetime
import matplotlib.pyplot as plt

filename="data/death_valley_2018_simple.csv"

dates, highs, lows = [], [], []

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# Handle errors in case of a missing data

	for row in reader:
		date = datetime.strptime(row[2], "%Y-%m-%d")
		try : 
			high = int(row[4])
			low = int(row[5])
		except ValueError:
			print(f"Missing data for {date}")
		else:
			dates.append(date)
			highs.append(high)
			lows.append(low)

plt.style.use("seaborn")
fig, ax = plt.subplots(figsize=(14,7))

ax.plot(dates, highs, c="red", alpha=0.7)
ax.plot(dates, lows, c="blue", alpha=0.7)
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.2)


plt.title("High and Low Temperatures for Death Valley for 2018", fontsize=20)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()