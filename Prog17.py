import numpy as np

# Define two 3x3 matrices
A = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])

B = np.array([[2, 1, 0],
              [1, 3, 2],
              [4, 0, 1]])
# Inverse of A
A_inverse = np.linalg.inv(A)
# Determinant of B
det_B = np.linalg.det(B)
# A . A inverse
result = np.dot(A, A_inverse)
print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nInverse of A:")
print(A_inverse)
print("\nDeterminant of B:")
print(det_B)
print("\nA multiplied by A inverse:")
print(result)