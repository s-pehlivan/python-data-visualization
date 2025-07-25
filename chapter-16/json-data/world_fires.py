import csv
from plotly.graph_objects import Layout
from plotly import offline

filename = 'data/world_fires_1_day.csv'

lats,lons, brightness_mags = [], [], []

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    for row in reader: 
      

        try:
            mag = float(row[2])
            lat = float(row[0])
            lon = float(row[1])
            brightness_mags.append(mag)
            lats.append(lat)
            lons.append(lon)
        except:
            print("magnitute is not in the correct type")


data = [{
	'type': 'scattergeo',
	'lon': lons,
	'lat': lats,
    'marker': {
		'size': [0.05*mag for mag in brightness_mags],
		'color': brightness_mags,
		'colorscale': 'Viridis',
		'reversescale': True,
		'colorbar': {'title': 'Magnitude'}
	}
}]

layout = Layout(title="World Fires")

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename='world_fires.html')



