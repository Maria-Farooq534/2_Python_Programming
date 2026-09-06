import numpy as np

# # Exercise 1

# marks = np.array([45, 67, 89, 32, 76, 91, 55, 84, 73, 100])

# # 1. Print:

# # total marks
# # average marks
# # highest mark
# # lowest mark
# # standard deviation

# print(f"Total marks: {np.sum(marks)}")
# print(f"Average: {np.sum(marks) / len(marks)}")
# print(f"Highest Marks: {np.max(marks)}")
# print(f"Lowest Marks: {np.min(marks)}")
# print(f"Standard Deviation: {np.std(marks)}")

# # 2. Create a Boolean mask for students who scored 70 or above.

# # print(marks >= 70)
# above_avg = marks >= 70
# print(above_avg)

# # 3. Use that mask to create a new array containing only students who scored ≥70.

# above_seventy = marks[marks >= 70]
# print(above_seventy)

# # 4. Count how many students scored ≥70.
# print(f"Count: {len(marks[marks >= 70])}")
# print(np.sum(marks>=70))

# # print(len(above_seventy))

# # 5. Replace every mark below 50 with 0.
# print(marks)
# print(np.where(marks >= 50 , marks, 0))

# # 6. Add 5 bonus marks to every student, but don't allow any final mark to exceed 100.
# print(marks)
# bonus = np.where(marks + 5 <= 100 , marks + 5, 100)
# print(bonus)



#### Exercise 02 : 2D ML-Style Dataset #########

x = np.array([
    [1200, 3, 10],
    [1500, 4,  5],
    [ 900, 2, 20],
    [1800, 4,  3],
    [1100, 3, 15],
    [2000, 5,  2]
])

x_features = np.array(['area' , 'bedrooms' ,  'age'])

# print(x.shape)
# print(x.ndim)
# print(x.size)

# print(x_features.shape)
# print(x_features.ndim)
# print(x_features.size)


# Part 2 — Select individual features


# m = x.shape[1]
for i in range(x.shape[1]):
    print(f"Feature Name: {x_features[i]}, \nValues: {np.array(x[:, i])}\n")
    
# Part 3 — Feature statistics
# Calculate average for all features

avg = np.average(x, axis=0)
print(avg)

# mean
print(np.mean(x, axis=0))

# Find all houses whose: area is greater than 1400 sqft
area = x[: , 0]
print(area)
area_14 = area >= 1400
print(area_14)

print(x[area >= 1400])
# or simply
print(x[x[:, 0] >= 1400])

# Find houses satisfying both:
# area > 1200
# AND
# age < 10
print("Area less than 1200 and age less than 10.")
print(x[(x[:, 0] > 1200) & (x[: , 2] < 10)])

# Modify a feature
# Suppose we discover that all house ages were recorded 2 years too high.
# Subtract 2 from the age column only

age = x[: , 2]
print(age)
print(age - 2)

#  or
print("Age")
print(x[:,2]-2)



y = np.array([250000, 320000, 180000, 400000, 230000, 450000])