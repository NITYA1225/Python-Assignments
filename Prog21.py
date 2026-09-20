# create a square matrix of 4x4 and find out the eigen values and eigen vectors of the matrix using scipy package in python.Also find P,L,U of the matrix using scipy package in python.
import numpy as np
from scipy.linalg import eig, lu

# Create a 4 x 4 square matrix
A = np.array([
    [4, 1, 2, 0],
    [1, 3, 0, 1],
    [2, 0, 5, 2],
    [0, 1, 2, 4]
])

print("Matrix A:")
print(A)

# Find eigenvalues and eigenvectors
eigenvalues, eigenvectors = eig(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

# Find P, L and U using LU decomposition
P, L, U = lu(A)

print("\nP Matrix:")
print(P)

print("\nL Matrix:")
print(L)

print("\nU Matrix:")
print(U)