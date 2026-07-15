# ========= Student Grade Manager =========

# 1. Add Student
# 2. View Students
# 3. Clear Records
# 4. Exit

student_list = []
def add_std():
    student_info = {}
    name = input("Enter student name: ")
    marks = float(input("Enter user marks: "))
    student_info["name"] = name
    student_info["marks"] = marks
    student_list.append(student_info)
    print(f"{student_info['name']}'s record added successfully!")


# def view_std():
#     try:
#         for stuent in student_list:
#             for key, value in 
        

while True:
    print("""
    ========= Student Grade Manager =========

    1. Add Student
    2. View Students
    3. Clear Records
    4. Exit
    """)
    
    user_input = int(input("Select a number from 1 to 4: "))
    
    if user_input == 4:
        break
    
    if user_input == 1:
        add_std()
        
    # elif user_input == 2:
    #     view_std()
    
print(student_list)