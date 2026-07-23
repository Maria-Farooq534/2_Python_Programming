""" 
Classes are the bluprints, we can make thousands of objects from a class
a class has variables and methods(functions)
"""

# __init__ sets up the instructions for the new objects we will create using the class.
# the word self in the func does not represent only a value of the object. it represents the entire object.
# It's just like we are not hard coding anything, we let Python replace the self every time with the object user creates. 

# __init__() initilizes the objects' data. here in this case, display() is responsible for displaying the data, or more specifically, names here.
# __init__() is called constructor or initlilizer . When we craete an object, python immediately calls this constructor.

class Student:
    def __init__(self, name, marks): # here name and marks: is the length of attributes defined by the class.
        self.name = name
        self.marks = marks
        self.school = "UOS"  # so here, even if we have created another attibute, but it does not mean the lenght of attributes defined by the class is 3. it is still 2.
        # self.school = "UOS" is the class attribute
        print("Object created!") # this is the print statememnt, will be printed everytime we create a Student object. In above lines, we just initilized the variables, we are not printing anything, but here we do.
    
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print("*" * 30)
        
    def __str__(self):
        return f"Name: {self.name} \nMarks: {self.marks} \nSchool: {self.school} \n{"*" * 30}"
    
    # def __len__(self): __len__() func for fixed lengths.
    #     return 3 
    
    def __len__(self):
        return len(self.__dict__)
    
    def update_marks(self, marks):
        self.marks = marks
        return marks
    
    def is_pass(self):
        marks = self.marks
        if marks >= 50:
            print("Pass!")
        else:
            print("Fail!")
            
    def percentage(self):
        total = 100
        marks = int(self.marks)
        percent = (marks / total ) * 100
        return f"{percent}%"
    
    def change_name(self, name):
        self.name = name
        return name
          
    
        # it means the length is fixed and always returns 2. bcz name and marks are the 2 attributes of init func.
        # what if user later add other attributes?
        # so, there are multiple ways we can define what the length will be.
        # it can be fixed
        # or it can be the total number of attributes an object can have.
        # so, later if user add more objects like student1.fav_color = "red" , it will be counted as well
        # so, how to do so?
        
         
student1 = Student("Maria" , 90)  # here Maria and 90 are the instance attributes. In instance attribute, each object stores its own value.
student2 = Student("Ali" , 40)
student3 = Student("Noor" , 91)
# student1.display()



print(str(student3))
print(student1)
print(student2) # this is how we can directly print the Studnet object.
text = student1.__str__()   # this, when to store the the returned value of the function and later we can use it for multiple purposes. but we usually do not use this, we use this:
text = str(student1) # we we do this, python automatically do student1.__str__() 
print(text)

email = f"Student:\n{student1}"
print(email)

student3.fav_color = "red"
print(len(student3))
student1.email = "maria@gmail.com"

print(student1.__dict__)
print(student2.__dict__)

print(len(student1.__dict__))
new = len(student1.__dict__)
print(f"The length of the dictionary is: {new}")
print("Checking length")
print(len(student1))

print(student1.__dict__)
student1.update_marks(94)
print(student1)
print(student1.__dict__)

student1.is_pass()
student2.is_pass()
print(student2.percentage())
print(student3.percentage())

print(student2.__dict__)
student2.change_name("Alex")
print(student2.__dict__)