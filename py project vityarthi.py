
print("daily personal expense tracker is set to run through ")
#initialize the data structure
#expenses is a list of dictionary

expenses = []

def add_expenses():
    print("----add new expense----")
    while True:
        try:
            amount = float(input("enter amount:"))
            if amount <=0:
                print("amount must be in positive value ")
                continue
            break
        except valueError:
            print("invalid input")
    name=input("enter item name :")
    expenses.append({'item':name,'amount':amount})

def view_expenses():
    #lists every expenses recorded
    #loop through the list and print each item 
    for e in expenses:
         print(f"{e['item']}-rupee{e['amount']}")

def total_expenses():
    total = sum(e['amount'] for e in expenses)
    print("total expenses:rupee",total)


#       Main Program Loop
    
def main_menu():
    "the main interface for the user"
    while True: 
        print("\n1 %%%%the menu of the grand personal finance tracker%%%")
        print("1.add new transactions (expense income)")
        print("2.view all transaction history")
        print("3.show monthly summary")
        print("4.exit program ")
        choice = input("enter the choice:")
        if choice =='1':
            add_expenses()
        elif choice == '2':
            view_expenses()
        elif choice =='3':
            total_expenses()
        elif choice =='4':
            print("\n exiting thank you for tracking your finance")
            break
        else:
            print(" invalidchoice  please try again by some other valid choice " )


main_menu()
