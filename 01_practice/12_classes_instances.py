class Student():
    school = "UOS"
    def __init__(self, name):
        self.name = name
        
student1 = Student("Maria")
print(student1.school)
print(student1.__dict__)

Student.school = "FAST"
print(student1.school)
print(student1.__dict__)
        