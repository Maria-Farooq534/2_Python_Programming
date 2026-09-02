import numpy as np

rng = np.random.default_rng() # default_rng is the random no generator function of numpy

number1 = rng.integers(1 , 7) # 1 is the lower limit and 7 is the upper limit. means the random number will be in btw 1 and 7.
print(number1)

# This above, without seed will give differnet number each time. 

# If we want the number to be consistent , we need to set the seed value to 1.

# rng = np.random.default_rng(1)
number = rng.integers(1, 7)
print(number)

# now the first number1, without seed is changing , but the 2nd with seed = 1 is consistent

# for readability, we can write it like this:
number2 = rng.integers(low = 1 , high = 8) # just for readability
print(number2)

# we can set the numbers, of how many random numbers we want to generate , like:

three_numbers = rng.integers(1, 7 , size=3)
print(three_numbers)


three_numbers = rng.integers(low = 1, high = 101 , size=3)
print(three_numbers) # Thats the 1D array

# for 2D array
array = rng.integers(low = 1 , high = 101 , size=(3,2))
print("2D array: " , array)


# For Floating Values
# np.random.seed(1)
# In uniform() , every number has equal probability to appear
n1 = np.random.uniform(-1 , 1 ) 
print(n1)

n1 = np.random.uniform(-1 , 1 , size = 3) 
print(n1)

n1 = np.random.uniform(low = -1 , high = 1 , size= (3,2)) 
print(n1)



# Shuffle array

array = np.array([1,2,3,4,5])
print(array)
rng.shuffle(array)
print(array)



# For random choice

colors = np.array(["Green", "Blue", "White" , "Black" , "Pink"])
print(colors)

color = colors.copy()
print(color)

rng.shuffle(color)
print(color)

print(colors)

rng.shuffle(colors)
print(colors)

# for choice

# color = np.random.default_rng().choice(colors) 
# we can write it as : 
color = rng.choice(colors)
print(color)

# more than 1

two_colors = np.random.default_rng().choice(colors , size=2)
print(two_colors)

# for two dimensional
print("2D")
two_colors = np.random.default_rng().choice(colors , size=(2,2))
print(two_colors)

emojis = np.array(['🍕', '🍔' , '🌭' , '🥞' , '🍿' , '🥖' , '🫓'])
emoji = np.random.default_rng().choice(emojis , size = (3,2))
print(emoji)