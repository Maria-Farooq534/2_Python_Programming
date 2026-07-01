# Mini Project
# Create a simple Calculator using functions.
# Functions:
# add(a, b)
# subtract(a, b)
# multiply(a, b)
# divide(a, b)

# Each function should return the answer, not print it.

def addition(a,b):
    return a + b

def subtract(a, b):
    return a - b

def division(a, b):
    return a / b

def multiplication(a, b):
    return a * b

while True:
    print("""
          ---------------------Menu----------------------
          1. Add
          2. Subtract
          3. Division
          4. Multiplication
          5. Exit
          
          """)
    
    user_input = int(input("Select a number for its corresponding operation: "))

    
    if user_input not in [1 ,2, 3, 4, 5]:
        print("Invalid choice! Please select from the menu.")
        continue
    
    if user_input == 5:
        break
    
    num1 = int(input("Enetr number 1: "))
    num2 = int(input("Enter num 2: "))
    
    if user_input == 1:
        add_result = addition(num1, num2)
        print(f"The addition of {num1} and {num2} is {add_result}")
        
    elif user_input == 2:
        subtract_result = subtract(num1 , num2)
        print(f"The subtraction of {num1} and {num2} is {subtract_result}")
        
    elif user_input == 3:
        div_result = division(num1, num2)
        print(f"The division of {num1} and {num2} is {div_result}")
        
    elif user_input == 4:
        multiple_result = multiplication(num1 , num2)
        print(f"The multiplication of {num1} and {num2} is {multiple_result}")