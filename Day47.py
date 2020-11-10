import numpy as np

arr = np.array([1, 2, 3])
print("Array with 1: \n", arr)
arr = np.array([[1, 2, 3],
               [4, 5, 6]])
print("Array with Rank 2: \n", arr)

arr = np.array((1, 3, 2))
print("\nArray created using " " passed tuple:\n", arr)


arrr = np.array([[-1, 2, 0, 4],
                 [4, -0.5, 6, 0],
                 [2.6, 0, 7, 8],
                 [3, -7, 4, 2.0]])
print("Initial Array: ")
print(arrr)

sliced_arrr = arrr[:2, ::2]
print("Array with first 2 rows and" " alternate columns(0 and 2):\n", sliced_arrr)

Index_arr = arrr[[1, 1, 0, 3], [3, 2, 1, 0]]
print("\nElements at indices (1, 3), " "(1, 2), (0, 1), (3, 9):\n", Index_arr)


matrix = np.array([[1,2,3],[4,5,6]])
print(matrix)
print("\n")
print(matrix.T)
