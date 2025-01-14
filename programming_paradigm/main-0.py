# main-0.py

import sys
from bank_account import BankAccount

def main():
    # Initialize BankAccount with a starting balance of 100
    account = BankAccount(100)

    # Ensure correct number of arguments
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse the command and amount from command-line arguments
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Perform the appropriate operation based on the command
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command. Available commands: deposit, withdraw, display.")

if __name__ == "__main__":
    main()
