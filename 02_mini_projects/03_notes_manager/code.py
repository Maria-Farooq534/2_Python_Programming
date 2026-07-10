# ========== Notes Manager ==========

# 1. Add Note
# 2. View Notes
# 3. Clear Notes
# 4. Exit

def add_note(note):
    with open("./02_mini_projects/03_notes_manager/notes.txt" , "a") as file:
        file.write(note)
        file.write("\n")
        print("User Note added successfully.")
        
    
def view_note():
    with open("./02_mini_projects/03_notes_manager/notes.txt" , "r") as file:
        content = file.read()
        if not content:
            print("No notes added! Please add notes first.")
        else:
            print("The User Notes are: ", content)

        
        
def clear_notes():
    with open("./02_mini_projects/03_notes_manager/notes.txt" , "r") as file:
        content = file.read()
        if not content:
            print("No Notes available to clear.")
            
        else:
            with open("./02_mini_projects/03_notes_manager/notes.txt" , "w") as file:
                pass
                print("Notes are Cleared!")

while True:
    print("""
        ========== Notes Manager ==========
        1. Add Note
        2. View Notes
        3. Clear Notes
        4. Exit
        """)
    
    user_choice = int(input("Select a number from 1 to 4: "))
    
    if user_choice == 4:
        break
    
    if user_choice == 1:
        user_note = input("Enter user note: ")
        add_note(user_note)   
             
        
    elif user_choice == 3:
        clear_notes()
        
        
    elif user_choice == 2:
        view_note()