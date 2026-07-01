numbers = [20, 30,6.8, 45, 90, 40, 50]

numbers.append(60)
numbers.remove(20)
print(f"Length is: {len(numbers)}")

print(numbers)
numbers.remove(90) # specify the value u wnt to remove
print(numbers)


numbers.pop(3) # Specifiy the index number you want to remove.
print(numbers)

# Length
print(f"Length is: {len(numbers)}")


# Functions

print(max(numbers))
print(min(numbers))
print(sum(numbers))

# Average
avg = sum(numbers) / len(numbers)
print(f"Average is: {avg}")


# Membership
names = ["Ali", "Alex", "Noor"]
print("Ali" in names)
print("Nooor" in names)


# Sorting
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

# Loop Through List

for name in names:
    print(f"My name is : {name}")
    

########################################


# Mini Practice 1
# Create:
# fruits = ["apple", "banana", "orange"]


fruits = ["apple", "banana", "orange"]

# Perform:
# append("mango")
fruits.append("mango")
print(fruits)
fruits.append("apple")
print(fruits)
fruits.remove("apple")
print(fruits)
# remove("banana")
fruits.remove("banana")
print(fruits)
# print length
print(len(fruits))
# print first fruit
print(fruits[0])
# print last fruit
print(fruits[-1])


########################################

# Mini Practice 2
# Take 5 marks from user.
# Example:
# 85
# 90
# 78
# 88
# 95
# Solution:

marks = input("Enter 5 subject marks seperated by comma : ")
print(type(marks))


# Store in list.
mark_list = marks.split(",")
print(mark_list)
print(type(mark_list))


# Print:

# Maximum:
print(f"Max is: {max(mark_list)}")
# Minimum:
print(f"Min is : {min(mark_list)}")
# # Average:

# ['23', '24', '67', '29', '60']

int_mark_list = []
for mark in mark_list:
    mark = int(mark)
    int_mark_list.append(mark)
print(int_mark_list)
avg_marks = sum(int_mark_list) / len(int_mark_list)
print(f"Average marks: {avg_marks}")

#########################################


# Mini Practice 3

# Create:

cities = ["Lahore", "Karachi", "Islamabad", "Sargodha"]

# Ask user:
# Enter city:
user_city = input("Enter your city: ").title()
print(f"User city: {user_city}")

# Check:
# city in cities
# Print True/False.

if user_city in cities:
    print(True)
else:
    print(False)


#########################################

# Topic 3 Mini Project
# Student Marks Analyzer

# Take 5 marks from user.

user_marks = input("Enter marks seperated by comma : ")
# Store in list.
mark_lists = user_marks.split(",")
# Display:
print(mark_lists)
# Marks: [85, 90, 78, 88, 95]
mark_list = []
for marks in mark_lists:
    marks = int(marks)
    mark_list.append(marks)
    
print(mark_list)
# Highest:
print(f"Highest marks: {max(mark_list)}")
# Lowest:
print(f"Lowest marks: {min(mark_list)}")
# Average:
average_marks = sum(mark_list) / len(mark_list)
print(f"Average marks: {average_marks}")
# Total:
print(f"Total marks: {sum(mark_list)}")
# Then show:

# Sorted Ascending:
mark_list.sort()
print(mark_list)
# Sorted Descending:
mark_list.sort(reverse=True)
print(mark_list)