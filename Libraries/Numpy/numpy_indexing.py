import numpy as np

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

print(num_array.shape)  
print(num_array.ndim)

# numpy indexing

print(num_array[0:2]) # strat from index 0, end index is exclusive. start from 0, goes to 1. exclude 2.

print("From Start: ")
print(num_array[: 3])  # from start to index 3, 3 exclusive 

print("all")
print(num_array[:])

print("start, end, step")
print(num_array[0:3:2]) # gives 1st and 3rd 


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
    ],
    [
        [27,28,29],
        [30,31,32],
        [33,34,35]
    ]
])

print("start, end , step")
print(num_array[0: 4: 2])


# Negative Indeing , make the step -ve

print("negative step of 1 will reverse the order of layers")
print(num_array[::-1])

print("negative step of 2 will reverse the order of laer with a step of 2")
print(num_array[::-2])


# Column Selection
print("Column selection: ")

print(num_array[1][:,2])  # here, [1] tels to select 1 layer, and then inside the layer 1, [:,2] , select all rows and the 3rd column.
print(num_array[1][: , 0])
print(num_array[1][:, -1])
print("With column indexing")
print(num_array[1][: , 0:2])
print("Column idexing with a step")
print(num_array[1][: , 0:3:2])  # gives column at index 0 and 2, 3 is xclusive.

print("Starting from idex 1 to end with step of 2")
print(num_array[1][: , 1::2])


print("Selecting both rows and columns")
print(num_array[0][0:2 , 0:2]) # first 2 rows, and then first 2 columns of these 2 rows

print("Last rows and columns elements")
print(num_array[0][1:3, 1:3])
print(num_array[0][0:2 , 1:3])
print("we can left end index as : ")
print(num_array[0][0:2 , 1:])
 

print("From the mid of the matrix")
print(num_array[0][0:2 , 1:3])