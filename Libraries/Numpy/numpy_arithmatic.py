import numpy as np

# Scalar

array = np.array([1.4,2.6,3.9])
# array = array - 1
print(f"Actual Array: {array}")
# Performing operations on array with scalar
print(array - 1)
print(array ** 2)
print(array * .5)

# Vectorized math functions
print(f"\nVectorized Operations")

print(np.square(array))   # square
print(np.sqrt(array))     # gives square root
print(np.squeeze(array))  

print(np.round(array)) # always round to the nearest integr
print(np.floor(array)) # round down
print(np.ceil(array))  # round up

print(np.pi)           # defaut value

# Calculating area
radius = np.array([1,2,3])
area = np.pi * radius**2
print(area)


# Element wise Arithmatic

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1 - array2)
print(array1 + array2)
print(array1 * array2)
print(array1 / array2)
print(array1 // array2)
print(array1 ** array2)

# comparison operations

marks = np.array([45,66,89,76,100,99,70,90])
print(marks == 100) # this is also an emelment wise comparison.
print(marks >= 50)
print(marks < 50)

marks[marks<50] = 0 # using conditionals
print(marks)

