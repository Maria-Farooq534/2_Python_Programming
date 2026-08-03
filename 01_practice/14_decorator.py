class Student():
    def __init__(self, name, marks):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        self.name = name
        self.marks = marks    # here self.marks is not simply a marks variable or function,. python secretly calls the seter when we say self.marks.
        
    def __str__(self):
        return f"Name: {self.name}\nMarks: {self.marks}\n{"*" * 30}"

    def __len__(self):
        return len(self.__dict__)
    
    
    @property # when we use @property, python creates a property object and store it in the class not in function.
    def marks(self):                                 # the func/method name must be marks. later if we add attribute to an object we will write self.marks = 90 , so so, here marks must be the same name. let say we do self.score = 90 , then the method must be named as score().
        return self._marks
    @marks.setter
    def marks(self, value):
        if not isinstance(value, int):
            raise TypeError("Marks must be in numbers")
        if value < 0 or value > 100:
            raise ValueError("Marks must in between 0 and 100.")
        self._marks = value                                         # this is where the data is stored.
                                            
student1 = Student("Maria" , 90)
print(student1.marks)
print(student1)              

student1.marks = 97
print(student1)

student1._marks = -70
print(student1.__dict__)
print(student1.marks)
print(len(student1))


"""

instead repeating validation logic in both init() and setter() , we simply apply it in setter and call it in init().

print(student1.marks)              # normally python returns an attribute for self.marks = 90 like here in this case student1.marks
coz, we have not added setter yet. once we add setter and then call self.marks , now even without ().
python will check the Student classs, and fins the marks as a property object.

Whenever code reads student.marks, Python calls the getter.
Whenever code assigns student.marks = value, Python calls the setter.


Why is _marks "private"?
Python doesn't truly make it private.
The underscore is a convention that tells other programmers:
"This is an internal implementation detail. Please don't touch it directly."
But Python programmers understand:
"I shouldn't do this unless I have a very good reason."

"""