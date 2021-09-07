import numpy as np

# a = np.arange(10)
# print(a)

# L = range(1000)
# print([i**2 for i in L])

# a = np.arange(1000)
# print(a**2)

# array
# a is 1D array
a = np.array([0, 1, 2, 3])
print(a)
print(a.ndim)
print(a.shape)
print(len(a))
# b is 2D array
b = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
print(b)
print(b.ndim)
print(b.shape)
print(len(b))
# c is 3D array
# c = np.array([[[1,2,3,],[4,5,6],[7,8,9]]])
c = np.array([[[0, 1], [2, 3]], [[4, 5], [6, 7]]])
print(c)
print(c.ndim)
print(c.shape)
print(len(c))

a = np.diag([2, 4, 6, 8])
print(a)
print(np.diag(a))
a = np.arange(10)
print(a.dtype)
a = np.arange(10, dtype='float64')
print(a)

print(a.dtype)

a = np.zeros((3, 3))
print(a)
print(a.dtype)
a = np.diag([1, 2, 3])
print(a)
print(a.dtype)
print(a[1][1])
a[2, 1] = 2
print(a)
a[2, 0] = 1
print(a)

a = np.arange(10)
print(a)
print("a[5] = ", a[5])
a[5:] = 10
print(a)
print("a[5] = ", a[5])
a = np.arange(10)
b = a[::2]
print(b)
print(np.shares_memory(a, b))

b[0] = 10
print(a)
print(b)
a = np.arange(5)
c = a[::].copy()
print(a)
print(c)
a[0] = 10
print(np.shares_memory(a, c))
print(a)
print(c)
a = np.arange(0, 100, 10)
print(a)
print(a[[2, 3, 2, 4, 2]])
a = np.array([1, 2, 3, 4, 5])
b = a+1
print(b)
