import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# If the plot function is given one array of data, it will use it as the coordinates on the vertical axis, and it will just use each data point's index in the array as the horizontal coordinate.
# plt.plot([1, 2, 4, 9, 5, 3])  # x-axis is 0, 1, 2, 3, 4, 5
# plt.show()

# You can also provide two arrays: one for the horizontal axis x, and the second for the vertical axis y:
# plt.plot([-3, -2, 5, 0], [1, 6, 4, 3])
# plt.axis([-4, 6, 0, 7])  # optional: change the axis [xmin, xmax, ymin, ymax].
# plt.show()

# Now, let's plot a mathematical function
# x = np.linspace(-2, 2, 500)
# y = x**2
# plt.plot(x, y)
# # Options to customize the plot:
# plt.title("Square function")
# plt.xlabel("x")
# plt.ylabel("y = x**2")
# plt.grid(True)
# plt.show()

# You can pass the 3rd argument to change the line's style and color. For example "g--" means "green dashed line".
# plt.plot([-3, -2, 5, 0], [1, 6, 4, 3], "g--")
# plt.show()

# You can plot multiple lines on one graph very simply: just pass x1, y1, [style1], x2, y2, [style2], ...
# plt.plot(
#     [0, 100, 100, 0, 0],
#     [0, 0, 100, 100, 0],
#     "r-",
#     [0, 100, 50, 0, 100],
#     [0, 100, 130, 100, 0],
#     "g--",
# )
# plt.axis([-10, 110, -10, 140])
# plt.show()

# Saving a figure to disk is as simple as calling savefig
# x = np.linspace(-1.4, 1.4, 30)
# plt.plot(x, x**2)
# plt.savefig("my_square_function.png", transparent=False)

# A matplotlib figure may also contain multiple subplots. These subplots are organized in a grid. To create a subplot, just call the subplot function.

# The simplest way to add a legend is to set a label on all lines, then just call the legend function.
# x = np.linspace(-1.4, 1.4, 50)
# plt.plot(x, x**2, "r--", label="Square function")
# plt.plot(x, x**3, "g-", label="Cube function")
# plt.legend(loc="best")
# plt.grid(True)
# plt.show()

# Matplotlib also supports non-linear scales, such as logarithmic or logit scales.

# Plotting 3D graphs is quite straightforward: when creating a subplot, set the projection to "3d".
# x = np.linspace(-5, 5, 50)
# y = np.linspace(-5, 5, 50)
# X, Y = np.meshgrid(x, y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
# figure = plt.figure(1, figsize=(12, 4))
# subplot3d = plt.subplot(111, projection="3d")
# surface = subplot3d.plot_surface(
#     X, Y, Z, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm, linewidth=0.1
# )
# plt.show()

# Histograms
# data = [1, 1.1, 1.8, 2, 2.1, 3.2, 3, 3, 3, 3]
# plt.subplot(211)
# plt.hist(data, bins=10, rwidth=0.8)
# plt.subplot(212)
# plt.hist(data, bins=[1, 1.5, 2, 2.5, 3], rwidth=0.95)
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()
