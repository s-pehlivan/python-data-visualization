import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk(10)
rw.fill_walk()

point_numbers = range(rw.num_points)

plt.style.use("classic")
fig, ax = plt.subplots()


ax.plot(rw.x_values, rw.y_values, linewidth=1.5, color="cyan")
ax.scatter(rw.x_values, rw.y_values, s=20, color="red", edgecolors="none")

plt.show()

