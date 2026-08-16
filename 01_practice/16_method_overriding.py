class Person:
    def introduce(self):
        print("Person")


class Student(Person):
    def introduce(self):
        print("Student")
        super().introduce()


class Researcher(Student):
    def introduce(self):
        print("Researcher")
        super().introduce()
        
        
student = Student()
student.introduce()