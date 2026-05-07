# a = 10
# b = 30

# c = a + b

# print("c:", c)

# array = [1, 2, 3, 4, 8]

# print("length:", len(array))

# print(array[len(array)-1])


# fruits = ['apples', 'oranges', 'berries']
# print("fruits:", fruits)
# fruits[0] = 'mangoes'
# print("updated fruits:", fruits)


# def add(x, y):
#     return x + y


# sum = add(3,5)
# print("sum:", sum)


import numpy as np


# A = np.array([
#     [2, 3],
#     [2, 2],
#     [4, 7]
# ])


# print(A[0][1])
# A[0][1] = 40
# print("A:", A)

# print("\n")
# AI = np.linalg.inv(A)

# print("AI:", AI)


# to check dimensions of a matrix

# dim = np.shape(A)

# print("dimensions:", dim)
# print("type of A:", type(A))


# B = np.ones((600, 500), dtype=np.int64)
# print("B:", B)

# print("dimensions of B:", np.shape(B))
# print("rows of B:", len(B))

# print("columns of B:", len(B[0]))

# C = np.zeros((5, 5), dtype=np.int64)
# print("C:", C)


# D = np.array([
#     [2, 3, 6],
#     [2, 2, 5],
#     [4, 7, 0]
# ])


# print(D[:,[0]])

# print(D[:, [0, 1, 2]])  # will return all entries of column 1 and 2


# Multiplication of arrays

# x = [1,2,3]
# y = [2,2,2]

# z = x * y

# print("z:", z)  # this will not work as expected, it will concatenate the lists instead of multiplying element-wise


# x = np.array([1,2,3])
# y = np.array([2,2,2])
# z = x * y

# print("z:", z)


matrixA = np.array([
    [1, 2],
    [3, 4]
])

matrixB = np.array([
    [5, 6],
    [7, 8]
])

# multAB = np.matmul(matrixA, matrixB)
# print("multAB:", multAB)


# Transpose of a matrix

matrixAT = matrixA.T
matrixBT = matrixB.T

print("matrixAT:", matrixAT)
print("matrixBT:", matrixBT)