import numpy as np

n = np.arange(1, 21)

matrix = (n ** 2 + 1).reshape(4, 5)

print("Original Matrix:")
print(matrix)

print("\nPattern:")
print("Each value is generated using the formula n² + 1.")
print("Consecutive values differ by consecutive odd numbers (3, 5, 7, 9, ...).")


double_matrix = matrix * 2

print("\nDouble Matrix:")
print(double_matrix)

mask = matrix % 5 == 0
count = np.sum(mask)


modified_matrix = matrix.copy()   
modified_matrix[mask] = -1

print("\nModified Matrix:")
print(modified_matrix)

print("\nNumber of values replaced:", count)