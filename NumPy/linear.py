# Matrix multiplication
# Determinant
# Matrix Inverse

import numpy as np
from numpy.linalg import inv, det
# Multiplication

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[1, 2, 3], [3, 4, 4], [5, 6, 5]])
C = A @ B
print(C)
X = np.matmul(A, B)
print(X)
Y = np.dot(A, B)
print(Y)

# Matric Inverse
# num=8
# num's reciprocal = 1/8
# num * num's reciprocal = 1
# inverse of number = 1/8

# in Matrix the reciprocal is called as Inverse
# A * A^-1 = I I= Identity Matrix
# Identity Matrix =diagonal must be same

AA = np.array([[4, 7], [2, 6]])
inverse_AA = inv(AA)
print(inverse_AA)

deteminant_AA = det(AA)
print(deteminant_AA)
print(int(deteminant_AA))


B = np.array([[118.5, 135.2]])
A = np.array([[3, 3.5], [3.2, 3.6]])
X = np.matmul(B, inv(A))
print(X)
child, adult = X.flatten()
print("Child: ", int(round(child)))
print("Adult: ", int(round(adult)))
