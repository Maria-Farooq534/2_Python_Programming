import numpy as np
print(np.__version__)

num_list = [1,2,3,4]
print(type(num_list))


print("0D array")
zeroD_array = np.array("1")
print(zeroD_array)
print(zeroD_array.ndim)


print("1D array")
num_array = np.array([1,2,3,4])
num_array *= 2
print(num_array)
print(type(num_array))


print("2D array")
num_array = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(num_array)
print(type(num_array))
print(num_array.ndim)


print("3D array")
num_array = np.array([
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ],
    [
        [10,11,12],
        [13,14,15],
        [16,17,18]
    ]
])

print(num_array.shape)  # now the layers are 2 here.
print(num_array.ndim)




print("3D array")
num_array = np.array([
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ],
    [
        [10,11,12],
        [13,14,15],
        [16,17,18]
    ],
    [
        [18,19,20],
        [21,22,23],
        [24,25,26]
    ]
])

print(num_array.shape)  # gives (3, 3, 3) where first 3 shows layers, 2nd 3 shows no of rows, and 3rd shows no of columns in 3D array.
print(num_array.ndim)





# Chain Indexing

# accessing specific elment of the ND array.

print(num_array[0]) # print the first layer of the nd array
print(num_array[0][0])  # firsy layer , and first row of the first layer
print(num_array[0][2])   # first layer , 3rd row

print(num_array[0][0][0])       # first layer, first row, and first column, this gives the frst elment of first row


# The fastest way to do is to use numpy multidimensional indexing
# It uses single sq bracket , and numbers are seprated by commas.

print(num_array[0,0,0])   # first layer, first row, first column.


numbers = num_array[0,0,0] + num_array[2,2,0] + num_array[2,2,0]
print(numbers)