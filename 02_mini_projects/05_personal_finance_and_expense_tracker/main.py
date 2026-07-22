import storage_helper

storage_helper.load_data()

while True:
    print("""
          ***** Menu *****
        1. Add Transaction
        2. View All Transactions
        3. View Category Summary & Unique Tags
        4. Save Data
        5. Exit
          """)
    
    # here user can enter a string like add transaction, so I'll use try except here.
    try:
        while True:
            user_choice = int(input("Enter a number from 1 to 5: "))
            if user_choice in range(0,6):
                break
            else:
                print("Invalid choice! Please choose a number from 1-5.")
                                
        if user_choice == 5:
            storage_helper.save_data()
            print("Goodbye")
            break
        
        if user_choice == 1:
            storage_helper.add_trans()
        
        elif user_choice == 2:
            storage_helper.view_trans()
            
        elif user_choice == 3:
            storage_helper.view_summary()
        
        elif user_choice == 4:
            storage_helper.save_data()
                    
            
    except ValueError:
        print("Invalid Choice. Please enter a number for corresponding option!")