from expense import income,expense,savingsGoal
from transcation import transcation_History,Finance_tracker

transcation_summary=transcation_History()
tracker_budget = Finance_tracker()

def main():
    print(" ",end='\n')
    print("EXPENSE TRACKER")
    while True:
        print(" ",end='\n\n')
        print("Where to do you want to begin with")
        print("1.Enter an income")
        print("2.Enter an expense")
        print("3.Set a saving Goal")
        print("4.Show remaining balance")
        print("5.Show transcation history")
        print("6.To exit from your expense tracker")

        print("****************************************************************************",end='\n\n')

        choice = input("Enter your choice (1-6): ")
        print(" ",end='\n\n')

        if choice == "1":
            print("Enter the required details")
            your_income = int(input("enter your income "))
            your_source = input("enter your source of income ")
            my_entity_income=income("income",your_income,your_source)
            my_entity_income.record_transcation()
            transcation_summary.record_transcation(my_entity_income.income_List[-1])
            tracker_budget.add_income(my_entity_income)
            add_savings = input("Do you want add any amount to savings enter YES/NO ")
            if my_entity_income.yes_or_no_to_boolean(add_savings):
                amount_to_savings = int(input("enter amount you want to transfer "))
                my_entity_savings=savingsGoal("savings")
                my_entity_savings.add_to_savings(amount_to_savings)
                transcation_summary.record_transcation(my_entity_savings.savings_List[-1])
                tracker_budget.add_savings_goal(my_entity_savings)
            else: 
                print("Okay..")
            

        elif choice == "2":
            print("Enter the required details")
            your_expense=int(input("enter your expense"))
            your_category_expense = input("enter on what did you spend ")
            my_entity_expense=expense("expense",your_expense,your_category_expense)
            my_entity_expense.record_transcation()
            transcation_summary.record_transcation(my_entity_expense.expense_list[-1])
            tracker_budget.add_expense(my_entity_expense)

        elif choice == "3":
            target_savings_amount = int(input("Enter savings goal amount: "))
            #my_entity=savingsGoal("savings")
            trans = my_entity_savings.set_savings_goal(target_savings_amount)
            if trans:
                transcation_summary.record_transcation(my_entity_savings.savings_List[-1])
                tracker_budget.add_savings_goal(my_entity_savings)
        

        elif choice == "4":
            print("Your remaining balance is ")
            tracker_budget.calculate_remaining_budget(my_entity_savings.total_savings)

        elif choice == "5":
            print("Transcation History")
            transcation_summary.print_transcation()
            
        elif choice == "6":
            print("Exiting the Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
