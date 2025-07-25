import json

from plotly.graph_objects import Layout
from plotly import offline

# Explore the structure of data
filename = 'data/eq_data_30_day_m1.json'

with open(filename) as f:
	all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data-30-days.json'

with open(readable_file, 'w') as f:
	json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
layout_title = 'Global Earthquakes'

try:
    layout_title = all_eq_data['metadata']['title']
except AttributeError:
    layout_title = 'Global Earthquakes'

layout_title = all_eq_data['metadata']['title']

mags, lons, lats, hover_texts = [], [], [], []


for eq_dict in all_eq_dicts:
	mags.append(eq_dict['properties']['mag'])
	lons.append(eq_dict['geometry']['coordinates'][0])
	lats.append(eq_dict['geometry']['coordinates'][1])
	hover_texts.append(eq_dict['properties']['title'])

# Map The Earthquakes
data = [{
	'type': 'scattergeo',
	'lon': lons,
	'lat': lats,
	'text': hover_texts,
	'marker': {
		'size': [5*mag for mag in mags],
		'color': mags,
		'colorscale': 'Viridis',
		'reversescale': True,
		'colorbar': {'title': 'Magnitude'}
	}
}]

my_layout = Layout(title=layout_title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename="global_earthquakes_colored.html")
 