import numpy as np


# # array
# a = np.array([1, 2, 3, 4])
# print("### a ###")
# print("position 1: ", a[1])  # 2
# print("shape: ", a.shape)  # (4,)

# # multi-dimensional array
# a_mul = np.array(
#     [
#         [1, 2, 3, 1],
#         [4, 5, 6, 1],
#         [7, 8, 9, 1],
#     ]
# )
# print("### a_mul ###")
# print("position 1: ", a_mul[1])  # [4, 5, 6, 1]
# print("shape: ", a_mul.shape)  # (3, 4)

# # multi-dimensional array with different dimensions in each position.
# a_mul_2 = np.array(
#     [
#         [
#             [1, 2, 3, 1],
#             [4, 5, 6, 1],
#             [7, 8, 9, 1],
#         ],
#         [
#             [1, 1, 1, 1],
#             [1, 1, 1, 1],
#             [1, 1, 1, 1],
#         ],
#     ]
# )
# print("### a_mul_2 ###")
# print("position 1: ", a_mul_2[1])  # position 1 is a 2D array.
# print("position 1, 1: ", a_mul_2[1, 1])  # position 1, 1 is a 1D array.
# print("shape: ", a_mul_2.shape)  # shape is a tuple (2, 3, 4).
# print("size: ", a_mul_2.size)  # size is the number of elements (24).
# print("ndim: ", a_mul_2.ndim)  # ndim is the number of dimensions (3).
# print("dtype: ", a_mul_2.dtype)  # dtype is the data type of the elements (int64).

# # multi-dimensional array of strings
# a_mul_string = np.array(
#     [
#         [1, 2, 3],
#         [4, "Hello", 6],
#         [7, 8, 9],
#     ]
# )
# print("### a_mul_string ###")
# print("dtype: ", a_mul_string.dtype)
# # dtype is now <U21 (unicode string of length 21) for all elements.

# # multi-dimensional array with a specific data type
# # the code below will throw an error,
# # because "Hello" cannot be converted to an integer.
# # a_mul_string = np.array(
# #     [
# #         [1, 2, 3],
# #         [4, "Hello", 6],
# #         [7, 8, 9],
# #     ],
# #     dtype=np.int64,
# # )
# # print("### a_mul_string ###")
# # print("dtype: ", a_mul_string.dtype)

# # multi-dimensional array with a specific data type (float)
# a_mul_float = np.array(
#     [
#         [1, 2, 3],
#         [4, "5", 6],
#         [7, 8, 9],
#     ],
#     dtype=np.float64,
# )
# print("### a_mul_float ###")
# print("dtype: ", a_mul_float.dtype)  # dtype is now float64 for all elements.
# print("dtype 1 1: ", a_mul_float[1][1].dtype)  # float64.
# print("position 1 1: ", a_mul_float[1][1])  # 5.0


###


# a_full = np.full((2, 3, 4), 9)
# print(a_full)

# a_zeros = np.zeros((2, 3, 4))
# print(a_zeros)

# a_empty = np.empty((2, 3, 4))
# print(a_empty) # it just allocates the memory without overwriting the values.

# x_values = np.arange(0, 100, 5)
# print(x_values) # [ 0  5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95]

# x_values = np.linspace(0, 1000, 4)
# print(x_values)  # [   0.          333.33333333  666.66666667 1000.        ]


### Special values


# print(np.nan)  # not a number
# print(np.inf)  # infinity

# print(np.isnan(np.nan))
# print(np.isinf(np.inf))

# print(np.sqrt(-1))  # nan (it also generates a RuntimeWarning).
# print(np.array([10]) / 0)  # [inf] (it also generates a RuntimeWarning).


### Math operations with arrays


# l1 = [1, 2, 3, 4, 5]
# l2 = [6, 7, 8, 9, 0]

# a1 = np.array(l1)
# a2 = np.array(l2)

# print(l1 * 2)  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# print(a1 * 2)  # [ 2  4  6  8 10]

# print(l1 + 2)  # error: TypeError: can only concatenate list (not "int") to list
# print(a1 + 2)  # [3 4 5 6 7]

# print(l1 - 2)  # error: TypeError: can only concatenate list (not "int") to list
# print(a1 - 2)  # [-1  0  1  2  3]

# print(l1 * l2)  # error: TypeError: can't multiply sequence by non-int of type 'list'
# print(a1 * a2)  # [ 6 14 24 36  0]

# a1 = np.array([1, 2, 3])
# a2 = np.array([[1], [2]])

# print(a1 + a2)  # [[2 3 4] [3 4 5]]

# a1 = np.array([1, 2, 3])
# a2 = np.array([[1, 1], [2]])

# print(a1 + a2)  # error: The requested array has an inhomogeneous shape

## Math functions on arrays

# a1 = np.array([[25, 36, 49], [64, 81, 100]])

# print(np.sqrt(a1))  # [[5 6 7] [8 9 10]]

# print(np.sin(a1))
# print(np.cos(a1))
# print(np.tan(a1))
# print(np.log(a1))
# print(np.log10(a1))
# print(np.exp(a1))
# ...


### array methods


# a = np.array([25, 36, 49])

# print(np.append(a, [7, 8, 9]))  # [25 36 49  7  8  9]
# print(a)  # [25 36 49]

# print(np.insert(a, 1, [7, 8, 9]))  # [25  7  8  9 36 49]
# print(np.delete(a, 1))  # [25 49]
