import numpy as np

a = np.array([[12, 15]])
b = np.array([[32, 65]])

print(a, b)
print(a+b)
# transpose
print( a.T )


print(a - b)

#scaller
s = 5
n = np.array([[20, 98]])

print(s*n)

# matrix multiplication
n = np.array([[11, 15]])
m = np.array([[4], [2]])
print(n*m)

print(np.dot(n,m))  # dot multiplication

# matrix sum
# print(a+b), where a and b are matrices

# identity matrix
IM1 = np.eye(2)
IM2 = np.eye(3)
print(IM1)
print(IM2)

# inverse of the matrix
a = np.array([[1,2,3,],[4,5,6],[7,8,9]])
print(np.linalg.inv(a))