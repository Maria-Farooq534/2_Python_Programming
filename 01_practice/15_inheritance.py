# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
    
#     def __str__(self):
#         return f"Name: {self.name}\nAge: {self.age}\nMarks: {self.marks}\n{"*" * 25}"
        
        
#     def introduce(self):
#         print(f"My name is {self.name}!")
    

# class Student(Person):
#     def __init__(self, name, age, marks):
#         super().__init__(name, age)
#         self.marks = marks
        

# student1 = Student("Maria" , 24, 90)
# print(student1)


# """
# if a child class has its own constructor, it overrides the parent class constructor __init__ .

# """

# class Person:
#     def introduce(self):
#         print("Hello")

# class Student: 
#     def introduce(self):
#         super().__init__()
#         print("I am a doctor.")
#         super().__init__()
        

# student = Student()     
# student.introduce()


class Person:
    def walk(self):
        print("Walking...")


class Student(Person):
    pass

student = Student() 
student.walk()



class Person:
    school = "UOS"
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def __str__(self):
        return f"Name: {self.name} \nAge: {self.age} \nMarks: {self.marks} \nschool: {self.school}"
       

student1 = Student("Maria" ,24, 90)
student2 = Student("Ali" ,30,  89)

print(student1)
print(student2)

    
# Parameters


class Parameters:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    
    
class Bias(Parameters):
    def __init__(self, name, number, bias_value):
        super().__init__(name, number)
        self.bias_value = bias_value
        
class Weights(Parameters):
    def __init__(self, name, number, weight):
        super().__init__(name, number)
        self.weight = weight
        

parameter = Parameters("parameters" , '2')
bias = Bias("Bias" , 1 , 0.1)
weights = Weights("Weight" , 2 , '10')

print("Parameters")
print(parameter.name)
print(parameter.number)

print("Bias")
print(bias.name)
print(bias.number)
print(bias.bias_value)

print("Weights")
print(weights.name)
print(weights.number)
print(weights.weight)