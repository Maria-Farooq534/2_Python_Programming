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
        
student3.marks = 500
print(student3)