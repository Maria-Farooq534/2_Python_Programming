# A variable created inside the function is called local variable and accessible only inside the function, not outside, 
# and destroys when function finishes.

def show_name():
    name = "Ali"
    print(name)

show_name()

##################

x = 10
def test():
    x = 25
    print(x)
    x = 20
    
    
test()
print(x)

# Python first search for x as a local variable, if could not find, then search for global variable x. its the execution order of python.
# If a variable is assigned inside the function, python treate it as local variable throuout the function and will not use any global variable for it.
# Python first decides a variable is local or global


# As soon as Python sees an assignment to a variable inside a function, it treats that variable as local throughout the entire function.
# The global keyword tells python not to make any local variable .

# Default Parameters

def std_name(name = 'Student'):
    print(f"Hello {name}!")
    print(f"Welcome {name}!")

std_name()

# The parameter has a default value, so even if no argument is passed, python use that default value for argument.
# But, if argument passed, python use that provided argument value. 
# The arguments override the default.

def power(number, exponent=2):
    print(number ** exponent)
    
power(2)
power(2,3)

# 2 is the default parameter value.
# 2 and 3 are the arguments


# Keyword Arguments
# We are explicitly specifying the argument value with its parameter.

def student(name,cgpa):
    print(f"{name} has {cgpa} CGPA!")
    
student(name="Maria" , cgpa=3.93)
# student(name="Maria" , 3.95) # it raise : SyntaxError: positional argument follows keyword argument
# Python Rule : Positional arguments must come before Keyword argument.
# For example
student("Maria" , cgpa=3.93) 
# Once we use keyword argument, every argument after that must be a keyword argument.


##########################################

x = 10

def user_value():


    global x
    print(x)
    x = 30
    print(x)
    # print(f"The value of x inside the function is : {x}")

user_value()    
print(f"The value of x outside the function is : {x}")    