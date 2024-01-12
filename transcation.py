from expense import financial_Entity,income,expense,savingsGoal

class transcation_History:
    
    transcations=[]
    def __init__(self,*args,**kwargs):
        self.args=args
        self.kwargs=kwargs
    
    #Records a financial transaction
    def record_transcation(self,transaction):
        self.transcations.append(transaction)
        
    def print_transcation(self):
        for i in range(0,len(self.transcations)):
            print(self.transcations[i])

class Finance_tracker(income,expense,savingsGoal):

    #Instances of Income, Expense, and SavingsGoal classes.
    def __init__(self):
        self.income_instances = []
        self.expense_instances = []
        self.savings_goal_instances = []

    def add_income(self, income_instance):
        self.income_instances.append(income_instance)

    def add_expense(self, expense_instance):
        self.expense_instances.append(expense_instance)

    def add_savings_goal(self, savings_goal_instance):
        self.savings_goal_instances.append(savings_goal_instance)

    #Calculates and returns the remaining budget.
    def calculate_remaining_budget(self,total_savings_goal):
        total_income = sum(income.amount for income in self.income_instances)
        total_expense = sum(expense.amount for expense in self.expense_instances)
        #total_savings_goal = sum(goal.target_amount for goal in self.savings_goal_instances)
        remaining_budget = total_income - total_expense - total_savings_goal
        print("remaining budget" + str(remaining_budget))
