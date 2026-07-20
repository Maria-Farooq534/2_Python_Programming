""" 
Classes are the bluprints, we can make thousands of objects from a class
a class has variables and methods(functions)
"""

# __init__ sets up the instructions for the new objects we will create using the class.
# the word self in the func does not represent only a value of the object. it represents the entire object.
# It's just like we are not hard coding anything, we let Python replace the self every time with the object user creates. 

class Student:
    def __init__(self, name, marks): # here for the student1 object, python make it like this: def __init__(student1, name, marks)
        self.name = name
        self.marks = marks
        
student1 = Student("Maria" , 90)
print(student1.name)
print(student1.marks)

class House:
    def __init__(self, area , location):
        self.area = area
        self.location = location

house1 = House(400 , "Sargodha")
print(house1.area)
print(house1.location)