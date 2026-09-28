class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"\nName: {self.name} \nAge: {self.age}"
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age_value):
        if not isinstance(age_value, int):
            raise TypeError("Age must be in numbers.")
        self._age = age_value
        
std1 = Student("Maria" , 24)
print(std1)

# std2 = Student("Maria" , '24') # gives error
std2 = Student("Aiman" , 25)
print(std2)

std3 = Student("Maria" , 24)
print(std3)


import numpy as np

# X = np.array([
#     [1200, 3, 10],
#     [1500, 4, 5],
#     [900,  2, 20],
#     [1800, 4, 3],
#     [1100, 3, 15]
# ], dtype=float)


X = np.array([
    [1200, 3, 10],
    [1500, 34, 5],
    [900,  2, 20],
    [1800, 4, 3],
    [1100, 9, 15]
], dtype=float)


def minmax_normalization(x):
    x_min = np.min(x, axis=0)
    x_max = np.max(x, axis=0)

    x_norm = (x - x_min) / (x_max - x_min)

    return x_norm


print("Original data:")
print(X)

x_min = np.min(X, axis=0)
x_max = np.max(X, axis=0)

print("\nMinimum values:")
print(x_min)

print("\nMaximum values:")
print(x_max)

X_minmax = minmax_normalization(X)

print("\nMin-Max normalized data:")
print(X_minmax)

print("\nMinimum after normalization:")
print(np.min(X_minmax, axis=0))

print("\nMaximum after normalization:")
print(np.max(X_minmax, axis=0))