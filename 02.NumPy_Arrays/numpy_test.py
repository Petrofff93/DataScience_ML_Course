import numpy as np

my_list = [1, 2, 3]
arr = np.array(my_list)
print(arr)

my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = np.array(my_mat)
print(matrix)

print(np.arange(0, 11, 2))
print(np.zeros(3))
print(np.zeros((5, 5)))

ones = np.ones((3, 4))
print(ones)

lspace = np.linspace(0, 5, 5)
print(lspace)

identity_matrix = np.eye(4)
print(identity_matrix)

rand = np.random.rand(5, 5)
print(rand)

randn = np.random.randn(5, 3)
print(randn)

randint = np.random.randint(1, 100, 5)
print(randint)

arr = np.arange(50)
ranarr = np.random.randint(0, 50, 10)

print(arr)
print(ranarr)

arr = arr.reshape(10, 5)
print(arr)

print(ranarr.max())
print(ranarr.argmax())
print(arr.shape)

print(arr.dtype)
