import numpy as np

# declare array
arr = np.array([1, 20, 2, 3, 2])
print(type(arr))
for item in arr:
    print(item)

# array with all elements 0 or 1
arr = np.zeros(5)
print(arr)
arr = np.ones(5)
print(arr)

# sort array
arr = np.array([1, 20, 2, 3, 2])
print(np.sort(arr))

# arr slicing
print(arr[1:2:2])

# arr operation
print(arr + 5)
print(arr - 5)
print(arr * 5)
print(arr // 5)

# find
print(np.where(arr == 2))

# shape size
arr = np.array([[1, 20, 2, 3, 2], [1, 20, 2, 3, 2]])
print(arr.ndim)
print(arr.shape)
arr = arr.reshape(5, 2)
print(arr)

# identity matrix
print(np.eye(3))

# arrange & linspace func
print(np.arange(-1, 10, 0.1))  # less than 10
print(np.arange(1, 10, 2))  # less than 10
print(np.linspace(1, 10))  # default 50
print(np.linspace(1, 10, 5))  # equal 10

# random array
print(np.random.rand(10))
print(np.random.rand(3, 3))

# diagnol matrix
print(np.diag([1, 2, 3, 4, 5]))

# flatten a matrix
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("matrix", a)
print("flattened matrix", a.flatten())

# trace a given matrix
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("matrix", a)
print("trace of matrix", a.trace())

# transpose of a matrix
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("given matrix", a)
print("transpose of matrix", a.T)

# -ve indexing in 2d array
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a[-1][-2])

# filtering array
a = np.array([1, 2, 3])
x = np.array([True, False, False])
print(a[x])
