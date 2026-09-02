import numpy as np
array1 = np.array([[1,2,3,4]])
array2 = np.array([
    [1],[2],[3],[4]
])

print(array1.ndim)
print(array2.ndim)

print(array1.shape)
print(array2.shape)


# broadcasting allows to perform opeations on arrays of different size.
# Rules for broadcasting
# Two arrays are compatible if:
# both of the dimensions have same size
# or
# one of the dimensions has the size 1
array3 = array1 * array2
print(array3)
print(array3.shape)
print(array3.ndim)

# it results in 4 by matrix. so, here we are virtually expanding our dimensions.

# WHat if the dimensions did not match:

a1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
a2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

print(a1.shape)
print(a2.shape)

a3 = a1 * a2
print(a3)
print(a3.shape)
print(a3.ndim)

# Aggregate functions , summarize data and typically returns single value
print("Aggregate functions")
array_1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])


print(np.sum(array_1))
print(np.mean(array_1))
print(np.std(array_1))
print(np.var(array_1))
print(np.max(array_1))
print(np.min(array_1))
print(np.argmax(array_1))  # returns the index no of max element
print(np.argmin(array_1))  # returns the index of number of min element

# Sum all columns

print(np.sum(array_1 , axis=0)) # sum of columns
print(np.sum(array_1 , axis=1)) # sum of rows



# Filtering : selecting elements from array that match conditions

ages = np.array([[33,13,16,78,45,34,23,12,19],
                [32,54,65,76,87,99,21,17,18]])

teenagers = ages[ages<18]
print(teenagers)

adults = ages[(ages >= 18) | (ages < 65)]
# adults = ages[(ages >= 18) & (ages < 65)]

print(adults)

seniors = ages[ages >= 65]
print(seniors)

evens = ages[ages % 2 == 0]
print("Evens: ", evens)

odds = ages[ages % 2 == 1]
print("Odds: ", odds)

adult = np.where(ages >= 18 , ages , 0) # it takes 3 arguments, first is condition, 2nd is the array itself on which the condition is applied , and 3rd is the value with which we will replace 
print(adult)

senior = np.where(ages >= 65 , ages , -1)
print(senior)

teenager = np.where(ages <= 18 , ages , np.nan)
print(teenager)