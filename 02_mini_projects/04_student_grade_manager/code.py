# ========= Student Grade Manager =========

# 1. Add Student
# 2. View Students
# 3. Clear Records
# 4. Exit

def add_std():
    name = input("Enter your name: ")
    while True:
        try:
            marks = int(input("Enter your marks in numbers: "))
            break
        except ValueError as e:
            print("Invalid format! Please enter marks in digits.")
        
    record = f"{name} - {marks}\n"
    with open("./02_mini_projects/04_student_grade_manager/student_record.txt" , "a") as file:
        file.write(record)
        # file.write(name)
        # file.write(" - ")
        # file.write(str(marks))
        # file.write("\n")
        print(f"{name}'s record added successfully.")
    
def view_std():
    try:
        with open("./02_mini_projects/04_student_grade_manager/student_record.txt" , "r") as file:
            content = file.read()
            if not content:
                print("No record found!")
            else:
                print(content)
    except FileNotFoundError:
        print("No student record management file exists.")

def clear_records():
    try:
        with open("./02_mini_projects/04_student_grade_manager/student_record.txt" , "w") as file:
            print("All records cleared!")
            pass
    except FileNotFoundError:
        print("No student record management file exists.")
    
             

while True:
    print("""
    ========= Student Grade Manager =========

    1. Add Student
    2. View Students
    3. Clear Records
    4. Exit
    """)
    
    try:
        user_input = int(input("Enter a number from 1 to 4: "))
        if user_input == 4:
            break
        
        if user_input == 1:
            add_std()
            
        elif user_input == 2:
            view_std()
            
        elif user_input == 3:
            while True:
                confirm_user = input("Are you sure you want to clear the records? y/n: ").lower()
                if confirm_user in ["n" , "no"]:
                    print("No records cleared!")
                    break
                elif confirm_user in ["yes" , "y"]:
                    clear_records()
                    break
                else:
                    print("Please select a valid option!")
            
    except ValueError:
        print("Invalid choice! Enter a valid number.")