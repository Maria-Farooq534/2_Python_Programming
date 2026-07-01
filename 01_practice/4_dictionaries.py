# student = {
#     "name" : "Maria",
#     "age" : 24,
#     "id" : 2,
#     "cgpa" : 3.9
# }

# print(student)

# # Access Vallues
# print(f"Student ID: {student["id"]}")


# # Modify Values
# student["age"] = 23
# print(student)


# # Add New Key
# student["gender"] = "Female"
# print(student)


# # Remove Keys
# # Method 1
# student.pop("gender")
# print(student)

# # Method 2
# del student['id']
# print(student)


# # Dictionary Methods
# print(student.keys())
# print(student.values())
# print(student.items())


# # Membership
# # Check if a key exists or not

# print("id" in student)
# print("name" in student)


# # get()
# # what if a key does not exists.
# # print(student["phone"])  # error, bcz phone does not exists

# print(student.get("phone"))
# print(student.get("phone" , "phone not exists"))

# # Loop through dictionary
# for key in student:
#     print(key)


# # Loop through dictionary values

# for key in student.values():
#     print(key)
    

# # For both key and value
# for key, value in student.items():
#     print(key, ":" , value)


# # Mini Practice 1
# # Create

# book = {
#     "title" : "Python Crash Course",
#     "author" : "Eric Mattes",
#     "Price" : "$500"
# }

# # Tasks

# # Print title
# print(book["title"])
# # Print author
# print(book["author"])
# # Change price
# book["Price"] = "$600"
# print(book.items())
# # Add publisher
# book["publisher"] = "unknown"
# print(book)
# # Delete publisher
# book.pop("publisher")
# print(book)

# ###############################

# # Mini Practice 2
# # Create

# car = {
#     "brand" : "Toyota",
#     "model" : "Corolla",
#     "year" : 2023
# }

# # Print

# # All keys
# print(car.keys())
# # All values
# print(car.values())
# # All items
# print(car.items())

# ###############################

# # Mini Practice 3

# # Ask user

# # Enter Name
# name = input("Enter your name: ")
# # Enter Age
# age = input("Enter your age: ")
# # Enter CGPA
# cgpa = input("Enter your cgpa: ")

# # Store in dictionary.
# user_info = {}
# user_info["name"] = name
# user_info["age"] = age
# user_info["cgpa"] = cgpa

# # Then print
# print(user_info)

# # Student Details

# # Name:
# print(f"Username is : {user_info.get("name")}")
# # Age:
# print(f"{user_info['name']} is {user_info['age']} years old.")
# # CGPA:
# print(f"{user_info['name']} has {user_info['cgpa']} cgpa.")

# # Use dictionary keys.

# ##############################


# # Mini Practice 4
# # Enter key:
# user_key = input("Enter a key : ")

# # If user enters
# # cgpa
# # Output
# # 3.85

# print(user_info.get(user_key, "not found"))

    
# # else:
# #     print(user_info.get("Not found"))

# # If user enters
# # salary
# # Output
# # Key not found

# # Use get() Do not use if.


################################################

# Topic 4 Mini Project
# Student Profile Manager

student = {
    "name" : "Maria",
    "id" : 2,
    "cgpa" : "3.9"
}

# Store one student in a dictionary.

while True:
    print("""
          ===== Student Profile Manager =====

    1. View Student
    2. Update CGPA
    3. Add City
    4. Delete City
    5. Exit

          """)

    # Ask User

    user_action = input("Choose an option from 1 to 5. : ")

    if user_action == "1":
        for key, value in student.items():
            print(key, ":" , value)



    elif user_action == "2":
        updated_cgpa = float(input("Enter updated cgpa : "))
        student["cgpa"] = updated_cgpa
        print("CGPA updated successfully.")
        


    elif user_action == "3":
        updated_city = input("Enter city to update: ")
        student["city"] = updated_city
        print("City updated successfully.")
        
        
    elif user_action == "4":
        removed_city = student.pop("city" , None)
        
        if removed_city is None:
            print("City not found.")
        else:
            print("City deleted successfully.")
    
        
    elif user_action == "5":
        break
    


# Each option should modify the dictionary.


book = {
    "title" : "Python Crash Course",
    "author" : "Eric Matthes",
    "price" : 3500,
    "available" : True
}

# Menu

print("""
      ===== Library Book Manager =====

1. View Book
2. Update Price
3. Change Availability
4. Add Publisher
5. Remove Publisher
6. Exit
      """)

# Solution

# Requirements
# Ask user for input

while True:
    user_choice = int(input("Choose from 1 to 6 : "))


    # Option 1: Display the book nicely.
    if user_choice == 1:
        for key, value in book.items():
            print(key, ":" , value)
            
            
    # Option 2: Ask the user for a new price.
    
    elif user_choice == 2:
        new_price = int(input("Enter updated price : "))
        book["price"] = new_price
        print("Price updated successfully.")
        
    
    # Option 3: Change Availability
    
    elif user_choice == 3:
        if book["available"]:
            book["available"] = False
            print("Book is not available.")
        else:
            book["available"] = True
            print("Book is available.")
    
        
    # Option 4: Add Publisher
    
    elif user_choice == 4:
        book["publisher"] = input("Enter publisher: ")
        print("Publisher added successfully.")
        
        
    # Option 5: Remove Publisher
    
    elif user_choice==5:
        book.pop("publisher" , "Publisher not found")
        
        
    else:
        break
        
####################################################


book = {
    "title": "Python",
    "price": 3500
}

x = book

print(id(book))
print(id(x))

x = book.copy()
x["price"] = 4000
print(book)
print(x)
print(f"Book id : {id(book)}")
print(f"X id : {id(x)}")

# Variables are labels attached to the objects,  Two variables can point to same or different objects.

####################################################################