def show_name():
    print("Name is: Maria")
    
    
def show_university():
    print("Studied in : University of Sargodha")
    
    

def show_cgpa():
    print("CGPA is: 3.9")
    
   
show_name()
show_university() 
show_cgpa()


########################################

# Main Program
def line():
    print("-------------------------------------")
    

def welcome():
    print("Welcome to Student Mangement System")

# Call them like this:
line()
welcome()
line()

# Output should be:

# ------------------------------
# Welcome to Student Management System
# ------------------------------

########################################

# Part 2: Parameters

def greet(name):
    print(f"Hello {name}!")
    
   
def show_square(num):
    square = num * num
    print(f"Square = {square}")


def student_info(name, cgpa):
    print(f"{name} has CGPA {cgpa}")
# Output:Maria has CGPA 3.95

def shows_square(num):
    return num * num


def add(a , b):
    return a + b


greet("Maria")
greet("Ali")
greet("Alex")

show_square(5)
show_square(8)
show_square(10)

student_info("Maria", 3.95)
student_info("Ali", 4.0)
student_info("Noor", 3.8)


result = shows_square(4)
print(result)
print(result * 5)

result1 = shows_square(8 * 2)
print(result1)

result2 = shows_square((8) + 2)
print(result2)

answer = add(1, 3)
print(answer)
print(answer * 2)
# Every function that does not explicitely return something, automatically returns None.


#########################################

# Practice 1
def multiply(a, b):
    return a * b

result = multiply(5,8)
print(result)

# Practice 2
def cube(num):
    return num ** 3

answer = cube(2)
print(answer)

# Practice 3

def full_name(first, last):
    return first + last

user_name = full_name("Maria ", "Farooq")
print(user_name)