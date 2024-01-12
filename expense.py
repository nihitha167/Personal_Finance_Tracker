class financial_Entity:

    name = None
    amount = 0
    transcation_List=[]

    def __init__(self,name,amount):
        self.name=name
        self.amount=amount
    
    #to record a financial transaction, providing a common interface for all financial entities.
    def record_transcation(self):
        pass
        
    #Returns details specific to the financial entity.
    def get_details(self):
        pass

    def yes_or_no_to_boolean(self,response):
        response_mapping = {'yes': True, 'no': False}
        return response_mapping.get(response.lower(), False)

class income(financial_Entity):

    source=None
    income_List=[]

    def __init__(self,name,amount,source):
        super().__init__(name,amount)
        self.source=source
    
    #Returns the income source
    def get_source(self):
        return self.source
    
    def record_transcation(self):
        self.income_List.append([self.name,self.amount,self.source])
        print(f"{self.income_List[-1]} transaction recorded")

    def get_details(self):
        return self.name,self.amount,self.source


class expense(financial_Entity):
    
    category_expense=None
    expense_list=[]

    def __init__(self,name,amount,category_expense):
        super().__init__(name,amount)
        self.category_expense=category_expense
    
    #Returns the expense category.
    def get_category(self):
        return self.category_expense
    
    def record_transcation(self):
        self.expense_list.append([self.name,self.amount,self.category_expense])
        print(f"{self.expense_list} transaction recorded")

    def get_details(self):
        return self.name,self.amount,self.category_expense

class savingsGoal(financial_Entity):

    target_savings_amount=0
    savings_progress = 0
    savings_List=[]
    total_savings=0

    def __init__(self,name,*args,**kwargs):
        self.name = name
        self.args=args
        self.kwargs=kwargs

    def print_savings(self,savings_amt,target_amt,amt,is_proceed):
        savings_amt = savings_amt+amt
        print("Your savings progress "+ str(savings_amt))
        if is_proceed:
            if target_amt-savings_amt == 0:
                target_amt = 0
                savingsGoal.target_savings_amount = 0 
                #savingsGoal.total_savings = savingsGoal.total_savings + savings_amt
                print("Reached goal")
                self.savings_List.append([self.name,target_amt,"add_to_savings"])
            else:
                print("Remaining amount to reach your goal "+str(target_amt-savings_amt))
                self.savings_List.append([self.name,target_amt-savings_amt,"add_to_savings"])
                savingsGoal.total_savings = savingsGoal.total_savings + savings_amt
        return savings_amt
        
    def add_to_savings(self,amount):
        if savingsGoal.target_savings_amount > 0:
            if savingsGoal.savings_progress < savingsGoal.target_savings_amount:
                savingsGoal.savings_progress = self.print_savings(savingsGoal.savings_progress,savingsGoal.target_savings_amount,amount,True)
            else:
                print("CONGRATS YOU ALREADY REACHED YOUR SAVINGS GOAL")
                update_goal = input("Do you want update your savings goal: enter YES/NO")
                if self.yes_or_no_to_boolean(update_goal):
                    temp = str(savingsGoal.target_savings_amount)
                    update_savings_goal = int(input("enter your desired saving goal , your current savings goal is "+temp))
                    savingsGoal.target_savings_amount = update_savings_goal
                    savingsGoal.savings_progress = self.print_savings(savingsGoal.savings_progress,savingsGoal.target_savings_amount,amount,True)
                else:
                    print("your amount is not added to savings account")
        else:
            print("Your savings goal is not set ")
            set_goal = input("would you like to set it before proceeding: enter YES/NO")
            if self.yes_or_no_to_boolean(set_goal):
                savings_amount = int(input("enter your savings goal "))
                savingsGoal.target_savings_amount = savings_amount
                savingsGoal.savings_progress = self.print_savings(savingsGoal.savings_progress,savingsGoal.target_savings_amount,amount,True)
            else:
                add_to_account = input("You didnt set any goal , do you still want to add to your savings account enter YES/NO")
                if self.yes_or_no_to_boolean(add_to_account):
                    savingsGoal.savings_progress = self.print_savings(savingsGoal.savings_progress,savingsGoal.target_savings_amount,amount,False)
                else:
                    print("not added to savings account")
        
    def set_savings_goal(self,amount):
        if savingsGoal.target_savings_amount > 0 :
            print("You already set the savings goal , which is "+ str(savingsGoal.target_savings_amount))
            change_goal = input("do you want to change enter YES/NO")
            if self.yes_or_no_to_boolean(change_goal):
                savings_amount = int(input("enter your savings goal "))
                savingsGoal.target_savings_amount = savings_amount
                print("New savings goal "+str(savingsGoal.target_savings_amount))
                if savingsGoal.savings_progress > 0 :
                    print("Reamining to save "+ str(savingsGoal.target_savings_amount-savingsGoal.savings_progress))
                    self.savings_List.append([self.name,savingsGoal.target_savings_amount,"set_savings_goal"])
                    return True
                else : 
                    print("Okay..")
                    return False
        else:
            savingsGoal.target_savings_amount = amount
            print(savingsGoal.target_savings_amount)
            print("Your savings goal is set"+ str(savingsGoal.target_savings_amount))
            self.savings_List.append([self.name,savingsGoal.target_savings_amount,"set_savings_goal"])
            if savingsGoal.savings_progress > 0 :
                if savingsGoal.target_savings_amount-savingsGoal.savings_progress == 0:
                    print("Reached goal")
                    savingsGoal.target_savings_amount=0
                else:
                    print("Remaining to save "+ str(savingsGoal.target_savings_amount-savingsGoal.savings_progress))
            return True



            

        













        