import numpy as np

X = np.array([
    [1200, 3, 10],
    [1500, 4, 5],
    [900,  2, 20],
    [1800, 4, 3],
    [1100, 3, 15]
])

print(np.mean(X, axis=0))
print(np.std(X, axis=0))

print(X.ndim)
print(X.shape)

def zscore_standardization(x):
    x_mean = np.mean(x, axis=0)
    x_std = np.std(x , axis=0)
    x_norm = (x - x_mean ) / x_std
    return x_norm

print(X)
x_scaled = zscore_standardization(X)
print(x_scaled)
print(np.mean(x_scaled, axis=0))
print(np.std(x_scaled, axis=0))

import numpy as np

X = np.array([
    [1200, 3, 10],
    [1500, 4, 5],
    [900,  2, 20],
    [1800, 4, 3],
    [1100, 3, 15]
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