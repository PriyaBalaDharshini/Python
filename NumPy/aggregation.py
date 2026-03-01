import numpy as np

array = np.array([11, 22, 33, 44])
print("Sum: ", np.sum(array))
print("Average: ", np.mean(array))
print("Median: ", np.median(array))
print("Max: ", np.max(array))
print("Min: ", np.min(array))

array2 = np.array([11, 22, 33, 44, 55])
print("Sum: ", np.sum(array2))
print("Average: ", int(np.mean(array2)))
print("Median: ", np.median(array2))
print("Max: ", np.max(array2))
print("Min: ", np.min(array2))

# Varience
# Variance=1/N N∑i=1 (xi−μ)2  μ=mean
print("Varience: ", np.var(array))

# Standard deviation = square root of varience
print("STD: ", np.std(array))


# 2D Array
arr2d = np.array([[2, 4, 6], [1, 3, 5]])
print("2D Sum: ", np.sum(arr2d))
print("2D Sum: ", np.sum(arr2d, axis=0))  # column addition
print("2D Sum: ", np.sum(arr2d, axis=1))  # row addition
print(
    "2D Sum: ", np.sum(arr2d[arr2d > 4])
)  # Addition with condition. Sum values more tha 4
