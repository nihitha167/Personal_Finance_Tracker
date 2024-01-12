# Personal_Finance_Tracker
Project in Python that uses object-oriented programming concepts

Overview
The Personal Finance Tracker is a command-line tool designed to help you manage your income, expenses, and savings goals. It provides a flexible and extensible platform for tracking financial transactions, calculating budgets, and setting savings targets.

Features
Income Tracking: Add various sources of income to keep a record of your earnings.
Expense Management: Categorize and track your expenses, ensuring a clear overview of where your money goes.
Savings Goals: Set and monitor savings, allowing you to plan for future expenses or aspirations.
Transaction History: Record all financial transactions comprehensively for historical tracking.
Budget Calculation: Calculate your remaining budget after accounting for income and expenses.

Classes and Structure
The project is organized around several classes to promote modularity and flexibility:
FinancialEntity: Base class for Income, Expense, and SavingsGoal. Common attributes and methods for financial entities.
Income: Derived from Financial Entity. Additional attributes for income sources.
Expense: Derived from FinancialEntity. Additional attributes for expense categories.
SavingsGoal: Derived from FinancialEntity. Additional attributes for savings goals.
TransactionHistory: Manages the recording and retrieval of financial transactions.
FinanceTracker: Main class managing income, expenses, savings goals, and providing budget calculations.

How to Use
Adding Income: Use the add_income method to add sources of income.
Adding Expenses: Utilize the add_expense method to add various expenses, optionally categorizing them.
Setting Savings Goals: Use the set_savings_goal method to set specific savings goals.
Calculating Totals: Employ calculate_total_income, calculate_total_expenses, and calculate_remaining_budget methods.
Categorizing Entries: For expenses, use the get_expenses_by_category method to retrieve expenses based on a specific category.
Transaction History: Record and retrieve financial transactions using the record_transaction and get_transaction_history methods.
