import pandas as pd
print(pd.__version__)

# Series: a 1D array

# data = [12,13,10,89]

# series = pd.Series(data)
# print(series)

# # for float
# data = [12.0,13.4,10.6,89.3]
# print(pd.Series(data))


# # for Bool
# data = [True, False, True, "True"]
# print(pd.Series(data))

# # for str
# data = ["True", "False", "True" , "B"]
# print(pd.Series(data))

# we can set custom labels, the default labels are index numbers , 0,1,2... 

data = [100, 102, 110, 120]
series = pd.Series(data, index=['a','b','c','d']) # we can pass a list, tuple, array
# print(series)
# print(series.loc["b"]) # loc is location by label, directly accessing the element by its label.
# print(series.loc["c"])
# # print(series.loc["d"]) # gives error bcz label did not exist.

print(series.iloc[0]) # accessing location w.r.t. index

print("Greaterthan or equal to 100: ")
print(series[series >= 110])
print(series[series < 100])


# Using dictionaries

models = {
    "Regression" : "Linear Reg",
    "Classification" : "CNN",
    "Clustring" : "K-Means"
}

series = pd.Series(models) # here we dont need to specify the index , and we will use labels as index number.

print(series)
print(f"Classification only : {series["Classification"]}")

print(series.loc['Clustring'])
print(series.loc['Classification'])
print("Using iloc: ")
print(series.iloc[2])


# Changing value 

series['Classification'] = 'SVM'
print(series.loc['Classification'])

print(series)