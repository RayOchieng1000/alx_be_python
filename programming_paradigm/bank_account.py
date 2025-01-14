# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the BankAccount with an initial balance (default is 0)."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a specified amount into the account."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw a specified amount from the account if sufficient funds are available."""
        if amount > self.account_balance:
            return False  # Insufficient funds
        elif amount > 0:
            self.account_balance -= amount
            return True
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """Display the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")
