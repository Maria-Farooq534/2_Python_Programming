import json
all_transactions = list()
def load_data():
    global all_transactions
    try:
        with open("./02_mini_projects/05_personal_finance_and_expense_tracker/transaction_records.json" , "r") as file:
            all_transactions = json.load(file)
            print("All transactions loaded successfully!")
    except FileNotFoundError:
        all_transactions = []

# Save Data function
    # dump() is a json function which means take this python object and dump it or write it into this file.
    # all_transactions : what to write (it contains the content what we have to write.)
    # file : its the file where to write.
    # indent = 4 is the format, means how to format the data.       
        
def save_data():
    with open("./02_mini_projects/05_personal_finance_and_expense_tracker/transaction_records.json" , "w") as file:
        json.dump(all_transactions , file , indent=4) 
        print("All records saved!")
        
        
def view_trans():
    if not all_transactions:
        print("No record found!")
    else:
        print("\n-------- All Records --------")
        for transaction in all_transactions:
            tag_string = ",".join(transaction["tags"]) if transaction["tags"] else "None"
            print(f"[Transaction Type: {transaction['trans_type'].upper()} | Transaction Description: {transaction["description"].title()} | Transaction Amount: {transaction['amount']} | Transaction Category: {transaction["category"]} | Transaction Tags {tag_string}]")
  

all_categories = {}
unique_tags = set()
def view_summary():
    if not all_transactions:
        print("No transaction summary found!")
        return
    
    for transaction in all_transactions:
        category = transaction["category"]
        amount = transaction["amount"]
        if category in all_categories:
            all_categories[category] = all_categories[category] + amount
        else:
            all_categories[category] = amount
    
    print("Category Summary: ")
    for cat, total in all_categories.items():
        print(f"{cat.capitalize()}: {total:.2f} ")
    
    for transaction in all_transactions:
        for tag in transaction["tags"]:
            cleaned_tag = tag.strip()
            if cleaned_tag:
                unique_tags.add(cleaned_tag)
                
    print("\n Unique Tags")
    if unique_tags:
        print(",".join(unique_tags))
    else:
        print("No tags found!")
        
    
        

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
    
    trans_record = {
        "trans_type" : trans_type,
        "description" : description,
        "amount" : amount,
        "category" : category,
        "tags" : all_tags   
    }
    
    all_transactions.append(trans_record)
    print(f"{trans_record} record added successfully!")