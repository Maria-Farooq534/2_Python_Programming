# # Practice 1 — Tuples
# student = ("Maria", 24, 3.95, "AI")

# # Tasks:

# # Print the name
# print(f"Student name is: {student[0]}")
# # Print the age
# print(f"{student[0]} is {student[1]} years old.")
# # Print the CGPA
# print(f"Cgpa : {student[2]}")
# # Print the department
# print(f"Student's department: {student[3]}")
# # Print the length
# print(f"Length is: {len(student)}")
# # Print the index of "AI"
# print(f"The index of AI is: {student.index('AI')}")
# # Print how many times 24 appears using count()
# print(f"Number of occurance of 24: {student.count(24)}")


######################################################

# # Practice 2 — Sets
# numbers = {10, 20, 20, 30, 40, 40}

# # Tasks:

# # Print the set
# print(numbers)  # it only shows a number once. so, it means set discard duplicates.
# # Add 50
# numbers.add(50)
# print(numbers)
# # Remove 20
# numbers.remove(20)
# print(numbers)
# # Try removing 100
# # numbers.remove(100) # it gives error
# # print(numbers)

# numbers.discard(100)
# print(numbers)
# # Use both remove() and discard() and observe the difference
# # Check if 30 exists
# print(f"30 in numbers exists? : {30 in numbers}")
# # Check if 70 exists
# print(f"70 in numbers exists? : {70 in numbers}")



# ######################################################

# # Practice 3 — Set Operations


# python_students = {"Ali", "Maria", "Noor", "Ahmed"}
# ml_students = {"Maria", "Ahmed", "Fatima", "Hamza"}

# # Union
# print(f"Union: {python_students | ml_students}")

# # Intersection
# print(f"Intersection: {python_students & ml_students}")

# # Difference
# print(f"The diffference of python-ml = : {python_students-ml_students}")
# print(f"The difference of ml-python = : {ml_students-python_students}")


##########################################################

# Topic 5 Mini Project
print("Student Attendance Manager")

# Ask the user to enter student names one by one.
print("Enter student names one by one and enter 'done' when completed.")
names = set()
while True:
    user_name = input("Enter student name: ")
    if user_name.lower() == "done":
        break
    names.add(user_name)
    print(f"Username '{user_name}' added successfully!")
    
    
    # if user_name != "done":
    #     names.add(user_name)
    #     print(f"Student name '{user_name}' added successfully!")
    # else:
    #     break
print(f"The unique students are: {names}")


# Then print:
# Unique Students:

print(f"Total unique students: {len(names)}")

# Total Unique Students: 3

# Notice that "Ali" should appear only once because we're using a set.

