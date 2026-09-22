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

def zscore_normalization(x):
    x_mean = np.mean(x, axis=0)
    x_std = np.std(x , axis=0)
    x_norm = (x - x_mean ) / x_std
    return x_norm

print(X)
x_scaled = zscore_normalization(X)
print(x_scaled)
print(np.mean(x_scaled, axis=0))
print(np.std(x_scaled, axis=0))