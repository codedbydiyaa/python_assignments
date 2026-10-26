import numpy as np

# Matrix Addition using Python List
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements of first matrix:")
A = [list(map(int, input().split())) for i in range(rows)]

print("Enter elements of second matrix:")
B = [list(map(int, input().split())) for i in range(rows)]

# Using Python Lists
C = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("Addition using Python Lists:")
for row in C:
    print(row)

# Using NumPy
A_np = np.array(A)
B_np = np.array(B)

print("Addition using NumPy:")
print(A_np + B_np)
