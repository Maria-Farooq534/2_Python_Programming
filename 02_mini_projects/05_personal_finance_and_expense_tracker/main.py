import storage_helper

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
            break
        
        if user_choice == 1:
            storage_helper.add_trans()
            
            
    except ValueError:
        print("Invalid Choice. Please enter a number for corresponding option!")