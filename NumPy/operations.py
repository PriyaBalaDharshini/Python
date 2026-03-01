import numpy as np

a = np.array([11, 22, 33])
b = np.array([50, 60, 70])
print(a + b)
print(a - b)
print(a * b)
print(b / a)
print(b // a)

# Broadcasting
a1 = np.array([34, 45, 56])
b1 = 6  # NumPy automatically converts into [6, 6, 6] no memory allowcation
print(a1 + b1)
print(a1 - b1)
print(a1 * b1)
print(a1 / b1)
print(a1 // b1)

arr1 = np.array([1, 2, 3])
arr2 = np.array([[2, 2, 2], [3, 3, 3]])
print("Broadcasted addition: \n", arr1 + arr2)

# aggregation
