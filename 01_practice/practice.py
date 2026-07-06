# ========== Student Result Management ==========
# 1. Add Student
# 2. View All Students
# 3. Search Student
# 4. Update CGPA
# 5. Delete Student
# 6. Exit

student_list = []
def add_std(std):
    print(f"{std} record added successfuly.")
    return student_list.append(std)
    

def view_std(std):    
    for student in student_list:
        print(f"The records for {student["name"].title()}: ")
        for key, value in student.items():
            print(f"{key} : {value}")
        print("-" * 30)
    if not student_list:
        print(f"No record found!")    
        
def search_std(std):
    found = False
    for student in student_list:
        if student["name"].lower() == std:
            print(f"{std.title()}'s record found: ")
            for key, value in student.items():
                print(f"{key} : {value}")
            found = True
            break
    if not found:
        print(f"No record found for {std.title()}!")
                
def update_cgpa(std):
    found = False
    for student in student_list:
        if student["name"].lower() == std:
            updated_cgpa = float(input("Enter updated CGPA: "))
            student["cgpa"] = updated_cgpa
            print(f"{std.title()}'s CGPA updated successfully!")
            found = True
            break
    if not found:
        print(f"Invalid choice! {std.title()}'s record is not available. Please select from available records!")
                      

def delete_std(std):
    found = False
    for student in student_list:
        if student["name"].lower() == std:
            student_list.remove(student)
            print(f"{student["name"].title()}'s record deleted successfully!")
            found = True
            break
    if not found:
        print(f"{std.title()}'s record didn't exists. Please select from avaialble records!")        
            
             

while True:
    
    print("""
    ========== Student Result Management ==========
    1. Add Student
    2. View All Students
    3. Search Student
    4. Update CGPA
    5. Delete Student
    6. Exit
    """)
    
    user_choice = int(input("Enter a number from 1 to 6: "))
    if user_choice == 6:
        break
    
    
    
    if user_choice == 1:
        name = input("Enter student name: ").lower()
        cgpa = float(input("Enter cgpa: "))
        dept = input("Enter department name: ")
        
        student_info = {}
        student_info["name"] = name
        student_info["cgpa"] = cgpa
        student_info["dept"] = dept
        
        result = add_std(student_info)

        
        
    elif user_choice == 2:
        view_std(student_list)
        
    
    elif user_choice == 3:
        std_to_search = input("Enter student name to search record: ").lower()
        search_std(std_to_search)
        
        
    elif user_choice == 4:
        std_to_update_cgpa = input("Enter student name to update their CGPA: ").lower()
        update_cgpa(std_to_update_cgpa)
        
        
    elif user_choice == 5:
        std_to_del = input("Enter student name to delete their record: ").lower()
        delete_std(std_to_del)