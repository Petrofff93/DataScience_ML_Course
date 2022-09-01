import numpy as np

arr = np.arange(0, 11)
slice_of_arr = arr[0:6]
slice_of_arr[:] = 99

arr_matrix = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

arr2 = np.arange(0, 11)
arr2 = arr2 + arr2
