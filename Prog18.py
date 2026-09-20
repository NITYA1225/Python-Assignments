import numpy as np
from scipy import linalg
A = np.array([[2, 3],
              [4, 5]])
B = np.array([8, 14])
solution = linalg.solve(A, B)
print("Solution:")
print("x =", solution[0])
print("y =", solution[1])