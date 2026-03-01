# Indexing
import numpy as np

arr = np.array([2, 4, 6, 8, 10, 1, 3, 5, 7, 9])
print(arr[4])

array = np.array([[2, 3, 4, 5], [6, 7, 8, 9], [10, 11, 12, 13]])
print(array[2][2])

# Slicing Extracting a sub array from the main array
# start:stop:step
print(arr[0:2])
print(arr[2:])  # from an index to the last element
print(arr[::])  # Start to end
print(arr[::-1])
print(arr[::-2])

print(array[1:3, 0:3])

# Boolean indexing
arr_bool = arr >= 5
print(arr_bool)
print(arr[arr_bool])

arr_bool1 = array >= 5
print(arr_bool1)
print(array[arr_bool1])

# Filtering
print(arr[arr > 4])

print(arr[(arr >= 3) & (arr % 3 == 0)])

print(array[array <= 7])

print(array[(array <= 7) & (array % 2 == 0)])
