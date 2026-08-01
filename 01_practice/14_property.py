class Student():
    def __init__(self, name, marks):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        self.name = name

        self.set_marks(marks)
        
    def __str__(self):
        return f"Name: {self.name}\nMarks: {self._marks}\n{"*" * 30}"

    
    @property
    def marks(self):
        return self._marks
    
    def set_marks(self, value):
        if not isinstance(value, int):
            raise TypeError("Marks must in integer.")
        if value < 0 or value > 100:
            raise ValueError("Marks must in between 0 and 100")
        self._marks = value
    
student1 = Student("Maria" , 90)
print(student1.marks)
student1.marks = 95
print(student1.marks)
