# Reshaping
# reshape: Used to change the shape of an array
# ravel: Flatterns multi dimentional array into 1D array
# flattern: Similar to ravel but return copy. CHanges do not affect the original array
# Stacking
# hstack: Joins arrays horizondally (along axis 1)
# vstack: Joins arrays vertically (along axis 0)
# concatenate: can concat along any axis
# Transpose
# swaps rows and columns
# using .T

import numpy as np

array = np.array([11, 22, 33, 44, 55, 66])
print("Original: ", array)

reshaped = array.reshape(3, 2)
reshaped1 = np.reshape(array, [2, 3])
print("Reshaped: ", reshaped)
print("Reshaped: ", reshaped1)

reshaped1[0][1] = 80
print(
    "Original: ", array
)  # original value will be changed becasue it does not create a copy. it directly modifies the original array
print("reshaped1: ", reshaped1)


array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("Original: ", array)
modified = array.ravel()
print("Ravel: ", modified)

modified[5] = 300
print("Original: ", array)
print("Value Modifed: ", modified)

array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
flatterned = array.flatten()
print("Original: ", array)
print("Value Faltterend: ", flatterned)

flatterned[4] = 345
print("Original: ", array)
print("Value Faltterend: ", flatterned)

array = np.array([1, 2, 3, 4])
array1 = np.array([5, 6, 7, 8])
print("Original: ", array, array1)

print(np.hstack([array, array1]))

print(np.vstack([array, array1]))

array = np.array([[1, 2, 3, 4], [11, 22, 33, 44]])
array1 = np.array([[5, 6, 7, 8], [55, 66, 77, 88]])
print("Original: ", array, array1)

print(np.hstack([array, array1]))

print(np.vstack([array, array1]))


array = np.array([1, 2, 3, 4])

array1 = np.array([5, 6, 7, 8])
print("Original: ", array, array1)

print(np.concatenate([array, array1]))

array2 = np.array([[1, 2, 3, 4], [11, 22, 33, 44]])
array3 = np.array([[5, 6, 7, 8], [55, 66, 77, 88]])
print(np.concatenate([array2, array3]))


array2 = np.array([[1, 2, 3, 4], [11, 22, 33, 44]])


print(array2.T)
print(array2.T.T)
