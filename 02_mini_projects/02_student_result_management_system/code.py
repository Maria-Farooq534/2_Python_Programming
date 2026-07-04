student_list = []

def add_std(std):
    student_list.append(std)
       
    
def view_std():

    for std in student_list:               
            for key, value in std.items():                
                print(f"{key} : {value}")
            print("-" * 30)
                
    if not student_list :
        print("No records found!")
       

def search_std(name_to_search):
    found = False
    
    for std in student_list:
        if std["name"].lower() == name_to_search:

            print(f"The results for {std["name"]} are: ")
                    
            for key, value in std.items():
                print(f"{key} : {value}")
                
            found = True
            break
    if not found:
        print(f"{name_to_search}'s records not found.")  # Never print "Not found" while you're still searching. (not in the loop)
            

def update_cgpa(std_name):
    found = False
    for std in student_list:
        if std["name"].lower() == std_name:
            std["cgpa"] = float(input("Enter updated CGPA: "))
            print(f"{std['name']}'s CGPA updated successfully!")
            found = True
            break
    if not found:
        print(f"{std_name}'s record not found!")
    

def delete_records(std_to_del):
    found = False
    for std in student_list:
        if std["name"].lower() == std_to_del:
            student_list.remove(std)
            print(f"{std_to_del}'s records deleted successfully!")
            found = True
            break
    if not found:
        print(f"{std_to_del}'s record not available.")

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
    
    user_input = int(input("Choose a number from 1 to 6 : "))
    if user_input == 6:
        break
    
    student = {}
    if user_input == 1:
        name = input("Enter Student Name: ")
        cgpa = float(input("Enter cgpa: "))
        dept = input("Enter dept name: ")
        
        student["name"] = name
        student["cgpa"] = cgpa
        student["dept"] = dept  
              
        print(f"The record: {student} added successfully.")
        add_std(student)

        
    elif user_input == 2:
        view_std()
        
    elif user_input == 3:
        std_to_search = input("Enter Student name to search records: ").lower()
        search_std(std_to_search)
        
    elif user_input == 4:
        std_to_update_cgpa = input("Enter student name whos CGPA has to update: ").lower()
        update_cgpa(std_to_update_cgpa)
        
    elif user_input == 5:
        std_to_delete = input("Enter Student name whos records to delete: ").lower()
        delete_records(std_to_delete)
        
        
    
    
