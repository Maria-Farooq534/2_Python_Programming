import numpy as np
X = np.array([
    [1200, 3, 10],
    [1500, 4, 5],
    [900,  2, 20],
    [1800, 4, 3],
    [1100, 3, 15]
], dtype=float)


def min_max(x):
    x_min = np.min(x, axis=0)
    x_max = np.max(x, axis=0)
    # print(x_min) contains 3 values in array for 3 columns
    # print(x_max)
    
    minmax = (x - x_min) / (x_max - x_min)
    return minmax


norm = min_max(X)
print(norm)