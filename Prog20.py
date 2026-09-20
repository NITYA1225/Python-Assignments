import numpy as np
from scipy import linalg
A = np.array([[1, 2],
              [3, 4]])
# QR decomposition
Q, R = linalg.qr(A)
print("Original Matrix A:")
print(A)
print("\nQ Matrix:")
print(Q)
print("\nR Matrix:")
print(R)
# SVD
U, s, Vh = linalg.svd(A)
print("\nU Matrix:")
print(U)
print("\nSingular Values:")
print(s)
print("\nVh Matrix:")
print(Vh)
# Least squares
b = np.array([5, 11])
x, residuals, rank, singular_values = linalg.lstsq(A, b)
print("\nLeast Squares Solution:")
print(x)
print("\nResiduals:")
print(residuals)
print("\nRank:")
print(rank)
print("\nSingular Values from lstsq:")
print(singular_values)