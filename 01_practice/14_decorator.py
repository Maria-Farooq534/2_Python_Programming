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

class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __str__(self):
        return f"\nName: {self.name} \nSalary: {self.salary}" 
    
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if not isinstance(value , (int, float)):
            raise TypeError("Salary must be in integer or float.")
        
        
        if value < 0 or value > 100000000:
            raise ValueError("Salary must be in between 10000 to 100000000.")
        
        # if not isinstance(value , float):
        #     raise TypeError("Salary must be in integer or float.")
        
        self._salary = value  
  
# 1              
employee1 = Employee("Maria" , 900000.0)        
print(employee1.name)
print(employee1.salary)
print(employee1)
print(employee1.__dict__)


employee1.salary = 99000876
print(employee1)
print(employee1.__dict__)


employee1._salary = 9657676
print(employee1)
print(employee1.__dict__)

# 2

e1 = Employee("Maria", 50000)

print(e1.salary)

e1.salary = 60000
print(e1.salary)

e1.salary = 600000-500
print(e1.salary)

e1.salary = 500 + 600000
print(e1.salary)

e1.salary = True
print(e1.salary)
# e1.salary = "60000"
# e1.salary = None


# practice challenge — Product
# Create a class called Product.
# It should have:
# name
# price
# stock
# Requirements:
# name should be stored normally.

# price must use @property + @price.setter.
# It must accept int or float.
# It must be between 0 and 1,000,000.
# Otherwise raise an appropriate error.

# stock must also use @property + @stock.setter.
# It must be an integer.
# It cannot be negative.
# Otherwise raise an appropriate error.

# Store the actual values internally as:
# _price
# _stock
# Add __str__() to display the product information.
# Create two products with different values.
# Test:
# reading product.price
# changing product.price
# reading product.stock
# changing product.stock
# an invalid price
# an invalid stock
# directly changing _price once, just to remind yourself that _price is still technically accessible.
# Solution:

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price 
        self.stock = stock
        
    def __str__(self):
        return f"\nName: {self.name} \nPrice: {self.price} \nStock: {self.stock}"
    
    def __len__(self):
        return len(self.__dict__)
    
    # Price

    @property
    def price(self):
        return self._price
        
    @price.setter
    def price(self, price_value):
        if not isinstance(price_value , (int, float)):
            raise TypeError("Price must be integer or float.")
        
        if price_value < 0 or price_value > 1000000:
            raise ValueError("Price must be in between 0 and 1000000.")
        
        self._price = price_value
        
    # Stock
    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, stock_value):
        if not isinstance(stock_value , (int, float)):
            raise TypeError("Stock must be an integer or float.")
        
        if stock_value < 0:
            raise ValueError("Stock  can't be a negative number.")
    
        self._stock = stock_value
        
    
price1 = Product("Laptop" , 900000 , 90)
print(price1)
price1._stock = -90
print(price1)