# Mini Project
# Create a simple Calculator using functions.
# Functions:
# add(a, b)
# subtract(a, b)
# multiply(a, b)
# divide(a, b)

# Each function should return the answer, not print it.

# Add
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2
def power(num1, num2):
    return num1 ** num2

while True:
    print("""
      Select a number for its corresponding operation:
      1. Add
      2. Subtract
      3. Multiplication
      4. Division
      5. Power
      6. Exit
      """)
    
    user_operation = int(input("Enter a number: "))
    
    if user_operation == 6:
        break
    
    if user_operation not in [1,2,3,4,5,6]:
        print(f"Invalid Input {user_operation}! Please select a number from the list")
        continue
    
    num1 = int(input("Enter number one: "))
    num2 = int(input("Enter number two: "))
    
    if user_operation == 1:
        addition_result = addition(num1,num2)
        print(f"The addition of {num1} and {num2} is: {addition_result}")       
    elif user_operation == 2:
        result = subtraction(num1, num2)
        print(f"The subtraction of {num1} and {num2} is: {result}")
    elif user_operation == 3:
        result = multiplication(num1, num2)
        print(f"The multiplication of {num1} and {num2} is: {result}")
    elif user_operation == 4:
        result = division(num1, num2)
        print(f"The division result of {num1} and {num2} is {result}")
    elif user_operation == 5:
        result = power(num1, num2)
        print(f"The number {num1} with power of {num2} is:  {result} ")