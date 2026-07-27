class Student():
    def __init__(self, name, marks):
        self.name = name
        
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100.") 
        else:
            self.marks = marks
        
    def __str__(self):
        return f"Name: {self.name}\nMarks: {self.marks}\n{"*" * 30}"


student1 = Student("Maria" , 99) 
# here 150 marks are not acceptable. but still it accepts.
print(student1)






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

"""