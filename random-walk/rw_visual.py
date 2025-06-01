import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk

count = 1

while True: 

	rw = RandomWalk(50_000)

	rw.fill_walk()

	# Plot the points in the walk
	plt.style.use("classic")
	fig, ax = plt.subplots(figsize=(10,2), dpi=300)

	point_numbers = range(rw.num_points)

	ax.scatter(rw.x_values, rw.y_values, s=1, c=point_numbers, cmap=plt.cm.Blues, edgecolors="none")

	#This will show the starting and ending points of the journey.

	# Call these scatter lines right before the plt.show() so that the plots would appear on top of all the other ones.
	# Starting Point
	ax.scatter(0, 0, c="green", edgecolors="none", s=10)
	# Ending point
	ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=10)

	# Remove axes

	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)


	# name = "rw_wall - " + str(count)
	# # plt.savefig(name, bbox_inches="tight")
	
	plt.show()

	count = count + 1

	keep_running = input("Make another walk? (y/n): ")
	if (keep_running == "n") :
		break