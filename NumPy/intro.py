import numpy as np

# 1D array
arr = np.array([10, 20, 30])
print(arr)

# 2D array
arr2d = np.array([[10, 20, 30], [40, 50, 60]])
print(arr2d)

# 3d array
arr2d1 = np.array([[1, 2, 3], [4.0, 5, 6], [7, True, 9]])
print(arr2d1)

arr3d = np.array(
    [
        [[1, 2, 3], [3, 4, 5], [3, 4, 5]],
        [[1, 2, 3], [3, 4, 5], [3, 4, 5]],
        [[1, 2, 3], [3, 4, 5], [3, 4, 5]],
    ]
)

print(arr3d.shape)

# Built-in properties
print(
    "Type:", type(arr)
)  # out: <class 'numpy.ndarray'> ndarray = Build-in data structure for numpy
print("Shape 1D", arr.shape)  # Shape 1D (3,) column
print("Shape 2D", arr2d.shape)  # Shape 2D (2, 3) row, column

print("Number of Elements: ", arr2d1.size)
print("Number of 3d Elements: ", arr3d.size)
print("Dimention of array: ", arr2d1.ndim)
print("Dimention of 3d array: ", arr3d.ndim)
print(
    "Datatype of array: ", arr2d1.dtype
)  # if all int = int64, anyone float float64, any one boolean float64
print(arr3d)
print("Shape 3D", arr3d.shape)  # Shape 3D (3, 3, 3) 3 layer, 3 rows 3 columns

array = np.array([[1, 2, 3], [1.0, 2.0, 3.0]], dtype=int)
print(array)
print(array.dtype)


# 3D Array
three = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original: ", three)
print("Size: ", three.shape)

arr2d1 = np.array([[1, 2, 3, 3], [4.0, 5, 6, 3], [7, True, 9, 3], [7, True, 9, 3]])
print(arr2d1)
print(arr2d1.shape)


zeros = np.zeros((5, 2), dtype=int)  # what numpy create = float by default
print("Zeros: ", zeros)

ones = np.ones((4, 3))
print("Ones: ", ones)

own = np.full((3, 5), 66)  # if we specify the value then its an int
print("Own: ", own)

empty = np.empty((3, 4))
print("Emptry: ", empty)  # array with carbage value with what curretly the memory has

spaced = np.linspace(0, 67, 8)  # 6 nubers from 0 to 1
print(f"Spaces: {spaced}")

arrr = np.arange(0, 44, 2)  # start stop and range
print(f"Array: {arrr}")


r = np.arange(12)
arr.reshape(4, 3)
print("R: ", r)