from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create 2 different D6
die_1 = Die()
die_2 = Die()
die_3 = Die()

results = [die_1.roll() * die_2.roll() * die_3.roll() for roll_num in range(1000)]

# Analyze the Result
max_result = die_1.num_sides * die_2.num_sides * die_3.num_sides
frequencies = [results.count(value) for value in range(1, max_result + 1)]

# Visualize the Result
x_values = list(range(1, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title" : "Result", "dtick": 10}
y_axis_config = {"title": "Frequency of Results"}

my_layout = Layout(title="Results of multilication for rolling three D6 1000 times", xaxis = x_axis_config, yaxis=y_axis_config)


offline.plot({"data": data, "layout": my_layout}, filename="d8_d8.html")