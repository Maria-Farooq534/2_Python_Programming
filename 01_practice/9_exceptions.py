age = int(input("Age: "))
# here if a user enter a string like "Maria" , it will be like age = int("Maria").
# here, python will check the first chacter , its M, it check is this a digit? No. can it be converted into digit? No
# so, the execution will stop here halfway. its not even completed. python will not even create the variable "age".

# input()
#    ↓
# "Maria"
#    ↓
# int()
#    ↓
# Conversion failed

# So, the assignment to "age" variable will not even happen. 

print(age + 10)  # If so, this line will not even be executed. python stops on line 1 and will not even execute line 2.


# try and except

try:
    print("A")
    x = int("B") # here the execution of try block stops,  python will raise a value error and except block excecution will start   
    print("C")
    
except ValueError:
    print("D")
    
    
# so, instead of having an error in the output, we just handled it properly.

try:
    print("User Age")
    age = int(input("Enter you age: "))
    print(f"User is {age} years old.")
    
except ValueError:
    print("Invalid Input. Enter age in digits.")

        
    
try:
    user_input = int(input("Enter age: "))
    print(f"User age is {user_input}")
    
except ValueError as e: # here 'e' is an objection object. its not the error, its the object storing that value error.
    print(e)
    

# Catching Different Types of Exceptions

try:
    print("A")
    x = 10 / 0
    print("B")
    
except:
    print("V")
    
print("Z")

try:
    user_age = int(input("Enter your age: "))
    result = 10 / user_age
    print(f"User is {result} years old.")
    
except ValueError as error:
    print("Invalid input! Please enter age in digits.")
    print(error)
    
except ZeroDivisionError as error:
    print("Age cannot be a zero! Please enter a valid number.")
    print(error)
    

try:
    user_input = int(input("Enter a number: "))
    print(user_input)
    square = user_input * user_input
    print(f"The square of the {user_input} is: {square} ")

except ValueError:
    print("Enter a valid number.")
    

try:
    number = int(input("Enter a number: "))
    print("A")

except ValueError:
    print("B")

else:
    print("C")

print("D")

try:
    print("A")
    x = int(input("Enter a number:"))

except ValueError:
    print("B")

finally:
    print("C")


try:
    print("A")
    x = int(input("Enter a number:"))

except ValueError:
    print("B")

finally:
    print("C")

print("D")

try:
    print("A")
    x = 10 / 0

except ValueError:
    print("B")

finally:
    print("C")

print("D")

