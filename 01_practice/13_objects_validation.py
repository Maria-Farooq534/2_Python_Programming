# class Student():
#     def __init__(self, name, marks):
#         self.name = name
        
#         if not isinstance(marks , int):
#             raise TypeError("Marks must be in numbers.")
            
#         elif marks < 0 or marks > 100:
#             raise ValueError("Marks must be between 0 and 100.")
        
#         self.marks = marks
        
#     def __str__(self):
#         return f"Name: {self.name}\nMarks: {self.marks}\n{"*" * 30}"


# student1 = Student("Maria" , 99) 

# print(student1)



"""
so, if the program is designed to have marks in btw 0 and 100. then the object should not accept any invalid number.
then what happens when user enter invalid number like 150 or -50?
should we tell user "Invalid input" and ask them to enter again?
no.
bcz, its a class, we dont have input() func so we can ask user to enter again
so,
the program fails and no object will be created with wrong values.



Notes:

This is the standard "fail fast" approach: if the constructor receives invalid data, 
it raises an exception instead of allowing an invalid object to exist.
Python actually allocates memory for the object before calling __init__().
If __init__() raises an exception, initialization fails and the assignment to student never completes, 
so you cannot use that object.

raise throws the exception
try/except catches the exception

"""


# Create a Student class with __init__().
# Add __str__().
# Add validation using TypeError and ValueError.
# Create four students:
# valid integer marks
# negative marks
# marks greater than 100
# string marks
# Observe which ones are created and which ones fail.

class Student():
    def __init__(self, name, marks):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        
        
        self.name = name
        
        if not isinstance(marks, int):
            raise TypeError("Marks must be in numbers")
        elif marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100.")
        
        self.marks = marks
        
        
    def __str__(self):
        return f"Name: {self.name}\nMarks: {self.marks}\n{"*" * 25}"
        


student1 = Student("Maria" , 90)
print(student1)
# student2 = Student("Maria" , -90)
# print(student2)
# student4 = Student("Maria" , 190)
# print(student4)
# student5 = Student("Maria" , "ninety")
# print(student5)

student3 = Student("Noor" , 90)
print(student3)
        
# now after this, we change the marks directly after the object is created, its changed again 
student3.marks = 500
print(student3)