# age = int(input("Enter your age: "))

# print(age)

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: You cannot divide a number by zero!")