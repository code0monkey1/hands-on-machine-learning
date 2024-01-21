import numpy as np
import numpy.linalg as linalg  # linear algebra functions


### System of linear scalar equations


# The solve function solves a system of linear scalar equations, such as:
# 2𝑥+6𝑦=6
# 5𝑥+3𝑦=−9

# coeffs = np.array([[2, 6], [5, 3]])
# depvars = np.array([6, -9])
# solution = linalg.solve(coeffs, depvars)
# print(solution)  # [-3.  2.]
# print(np.allclose(coeffs.dot(solution), depvars))  # True


### Vectorization


# Instead of executing operations on individual array items, one at a time, your code is much more efficient if you try to stick to array operations. This is called *vectorization*. This way, you can benefit from NumPy's many optimizations.
# For example, let's say we want to generate a 768x1024 array based on the formula $sin(xy/40.5)$. A **bad** option would be to do the math in python using nested loops:
# import math
# data = np.empty((768, 1024))
# for y in range(768):
#     for x in range(1024):
#         data[y, x] = math.sin(x * y / 40.5)  # BAD! Very inefficient.

# Let's vectorize this algorithm. First, we will use NumPy's meshgrid function which generates coordinate matrices from coordinate vectors.
# x_coords = np.arange(0, 1024)  # [0, 1, 2, ..., 1023]
# y_coords = np.arange(0, 768)  # [0, 1, 2, ..., 767]
# X, Y = np.meshgrid(x_coords, y_coords)
# # Now, both X and Y are 768x1024 arrays, and all values in X correspond to the horizontal coordinate, while all values in Y correspond to the vertical coordinate.
# # Now we can simply compute the result using array operations:
# data = np.sin(X * Y / 40.5)
# print(data)


### IN PROGRESS ###
# https://colab.research.google.com/github/ageron/handson-ml3/blob/main/math_linear_algebra.ipynb
