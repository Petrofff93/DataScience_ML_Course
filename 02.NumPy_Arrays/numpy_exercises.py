import numpy as np

# Create array with 10 zeros
arr_of_ten_zeros = np.zeros(10)
# Create array with 10 ones
arr_of_ten_ones = np.ones(10)
# Create array with 10 fives
arr_of_ten_fives = np.ones(10) * 5

# Create array from 10 to 50
array_from_ten_to_fifty = np.arange(10, 51)
# Create array from 10 to 50 with even nums
array_ten_to_fifty_evens = np.arange(10, 51, 2)

# Create 3x3 matrix with nums 0 to 9
three_by_three_matrix = np.arange(0, 9).reshape(3, 3)

# Create 3x3 identity matrix (ones on primary diagonal)
three_by_three_identity_matrix = np.eye(3)

gen_random_num = np.random.rand(1)
gen_x_count_nums = np.random.randn(25)

# I should create a shown matrix - 1st version
create_following_m = np.arange(1, 101).reshape(10, 10) / 100

# Second version
create_following_m2 = np.linspace(0.01, 1, 100).reshape(10, 10)

# Create an array of 20 linearly spaced points between 0 and 1
lin_arr = np.linspace(0, 1, 20)


# Matrix indexing

matrix = np.arange(1, 26).reshape(5, 5)

# Access 12,13,14,15 \n 17,18,19,20 \n 22,23,24,25
matrix = matrix[2:, 1:]

# Next we have to access just the number 20
matrix = matrix[1][3]

# Next we want 2 \n 7 \n 12
matrix2 = np.arange(1, 26).reshape(5, 5)
matrix2 = matrix2[:3, 1:2]

# We want 21, 22, 23, 24, 25
matrix3 = np.arange(1, 26).reshape(5, 5)
matrix3 = matrix3[4, :]

# We want 16, 17, 18, 19, 20 \n 21, 22, 23 ,24, 25

matrix4 = np.arange(1, 26).reshape(5, 5)
matrix4 = matrix4[3:, :]

# We want the sum of all items in the matrix

matrix5 = np.arange(1, 26).reshape(5, 5)
result = matrix5.sum()

# Get the standard deviation of the values in matrix5
result2 = matrix5.std()

# Get the sum of all the columns in matrix5
# We could specify an axis in order to get the wanted res
result3 = matrix5.sum(axis=0)
