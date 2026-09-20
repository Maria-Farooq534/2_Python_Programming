class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"\nName: {self.name} \nAge: {self.age}"
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age_value):
        if not isinstance(age_value, int):
            raise TypeError("Age must be in numbers.")
        self._age = age_value
        
std1 = Student("Maria" , 24)
print(std1)

# std2 = Student("Maria" , '24') # gives error
std2 = Student("Aiman" , 25)
print(std2)