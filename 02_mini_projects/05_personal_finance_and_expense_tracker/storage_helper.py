all_transactions = []
def add_trans():
    trans_type = input("Is this income or expense? i/e: ").lower()
    if trans_type in ["i" , "e" , "income" , "expense"]:
        pass
    else:
        print("Invalid choice! Please enter a valid option.")
    
    
    # for printing the result in better way, I'll keep full words instead of i and e.
    trans_type = "income" if trans_type in ["i" , "income"] else "expense"
  
    
    # transcation description
    description = input(f"Enter a short description of your {trans_type}: ")
    
    # amount , I'll use try except bcz user may enter amount in words. but i want in numbers.
    while True:    
        try:
            amount = float(input("Enter amount in numbers: "))
            break
        except ValueError:
            print("Invalid Input! Please enter amount in digits.")
    
    # transaction category
    category = input("Enter category e.g: food, shopping, salary: ")
    
    # tags
    tags = input("Enter tags seperated by commas: ")    
    all_tags = tags.split(",")
    
    # user can skip this by pressing enter, I'll add this functionality later.
    
    trans_record = {}
    trans_record["trans_type"] = trans_type
    trans_record["description"] = description
    trans_record["amount"] = amount
    trans_record["category"] = category
    trans_record["tags"] = all_tags
    
    all_transactions.append(trans_record)
    
    print(f"{trans_record} record added successfully!")

    
    # trans_record = [
    #     f"Transaction Type: {trans_type}\n",
    #     f"Transaction Description: {description}\n",
    #     f"Transaction Amount: {amount}\n",
    #     f"Transaction Category: {category}\n",
    #     f"Additional Tags: {all_tags}\n"
    # ]
    
    # try:
    #     with open("./transactions_record.txt" , "a") as file:
    #         file.write(str(trans_record))
    # except FileNotFoundError:
    #     print("No file exists!")