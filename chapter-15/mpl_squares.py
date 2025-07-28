import matplotlib.pyplot as plt

x_values = range(1,5000)
y_values = [x**3 for x in x_values]

plt.style.use("seaborn")

fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.twilight, s=10)

ax.set_title("Cube of Number", fontsize=24)
ax.set_xlabel("Numbers", fontsize=14)
ax.set_ylabel("Cubes", fontsize=14)

ax.tick_params(axis="both", which="major", labelsize=9)

ax.axis([0,5100, 0, 150000000000])

plt.show()




# x_values =  range(1, 6)
# y_values = [x**3 for x in x_values]

# plt.style.use("seaborn")
# fig, ax = plt.subplots()

# ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.twilight,  s=10)

# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Values", fontsize=14)
# ax.tick_params(axis="both", which="major", labelsize=14)

# ax.axis([0, 1100, 0, ])

# plt.savefig("squares_plot.png", bbox_inches="tight")

