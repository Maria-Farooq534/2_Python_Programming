cities = ("lahore" ,  "karachi" , 34 , 5)
print(cities[-1])
print(cities[1])
print(cities[1:3])


# Useful Functions
numbers = (10,50,60,30,50,80,90,100)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(len(numbers))

# count() : To count a specific Value in touple

print(f"50's are {numbers.count(50)}")
print(f"10's are {numbers.count(10)}")

# index() : tells the index number of a specific value

print(numbers.index(80))
print(cities.index("karachi"))


###########################################
# Sets
###########################################

fruits = {"banana", "apple", "orange", "mango"}
print(fruits)
fruits.add("grapes")
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.discard("banana")
print(fruits)

# Membership

print("banana" in fruits)
print("orange" in fruits)

# Set Operations

A = {1,9,3,4}
B = {0,1 ,4,5}
# Union
print(A | B)
# Intersection
print(A & B)
# Difference
print(A - B)

names = {"Ali", "Sara", "Alex", "Noor", "1"}
print(names)
names = {"Ali", "Sara", "Alex", "Noor", "Ali"}
print(names)
names = set(names)


A = {"Patient1", "Patient2", "Patient3", "Patient4"}

B = {"Patient3", "Patient4", "Patient5"}

print(A & B)
# It gives {'Patient3', 'Patient4'}, so this tells us that these 2 elements are duplicated in the datasets. this tells about the data leakgae.

# Let say , we have a dataset
train_case = {2,3,4,5,6}
test_case = {6,7,8,9,0}

data_leakage = train_case & test_case
print(data_leakage)