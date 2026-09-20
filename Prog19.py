import numpy as np
from scipy import linalg
# Create a 4x4 matrix
A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

# Transpose
transpose = A.T
# Rank
rank = np.linalg.matrix_rank(A)
print("Original Matrix:")
print(A)
print("\nTranspose of Matrix:")
print(transpose)
print("\nRank of Matrix:")
print(rank)