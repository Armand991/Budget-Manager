import json

# Simple budget manager
class BudgetManager:
    def __init__(self, budget):
        """Initialize the budget and create an empty list for expenses."""
        self.budget = budget  # Total budget in Rwandan Francs (RWF)
        self.expenses = []  # List to store expense records
    
    def add_expense(self, amount, category, description=""):
        """Adds a new expense to the expense list and checks the budget."""
        if amount <= 0:
            print("Invalid amount. Expense should be greater than zero.")
            return
        
        # Append expense details as a dictionary to the expenses list
        self.expenses.append({"amount": amount, "category": category, "description": description})
        self.check_budget()
    
    def get_total_expense(self):
        """Calculates and returns the total money spent."""
        return sum(expense['amount'] for expense in self.expenses)
    
    def get_remaining_budget(self):
        """Calculates and returns the remaining budget."""
        return self.budget - self.get_total_expense()
    
    def check_budget(self):
        """Checks if the user is approaching or exceeding their budget."""
        total_spent = self.get_total_expense()
        remaining = self.get_remaining_budget()
        
        print(f"Total Spent: {total_spent} RWF | Remaining Budget: {remaining} RWF")
        
        # Notify the user if they have exceeded or are close to exceeding their budget
        if remaining <= 0:
            print("Warning: You have no money left!")
        elif remaining < (self.budget * 0.1):
            print("Alert: You are about to finish your budget.")
    
    def save_data(self, filename="budget_data.json"):
        """Saves the budget and expense data to a JSON file."""
        data = {"budget": self.budget, "expenses": self.expenses}  # Dictionary to store budget details
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print("Data saved successfully.")
    
    def load_data(self, filename="budget_data.json"):
        """Loads budget and expense data from a JSON file."""
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.budget = data["budget"]  # Retrieve budget value
                self.expenses = data["expenses"]  # Retrieve list of expenses
                print("Data loaded successfully.")
        except FileNotFoundError:
            print("No saved data found.")

# Run the budget program
if __name__ == "__main__":
    # Ask the user to enter their budget
    budget = float(input("Enter your budget (RWF): "))
    manager = BudgetManager(budget)  # Create an instance of BudgetManager
    
    while True:
        # Display menu options
        print("\nOptions: 1. Add Expense 2. View Budget 3. Save & Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            # Add an expense
            amount = float(input("Enter amount (RWF): "))
            category = input("Enter category: ")
            description = input("Enter description (optional): ")
            manager.add_expense(amount, category, description)
        elif choice == "2":
            # View remaining budget
            print(f"Remaining Budget: {manager.get_remaining_budget()} RWF")
        elif choice == "3":
            # Save data and exit
            manager.save_data()
            break
        else:
            print("Invalid choice. Try again.")
