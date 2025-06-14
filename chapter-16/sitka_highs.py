import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = "data/sitka_weather_2018_simple.csv"

# Open the file and get the header names with next()
dates, highs = [], []

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# Get the high temperatures from this file.
	for row in reader: 
		high = int(row[5])
		date = datetime.strptime(row[2], "%Y-%m-%d")
		dates.append(date)
		highs.append(high)

# Plot the temperature highs
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red")

# Format plot
plt.title("Daily high temperatures, July 2018", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)


plt.show()