import json
import random
import os

class BankAccount:
    def __init__(self, account_holder_name, balance, account_number):
        self.account_holder_name = account_holder_name
        self.balance = balance
        self.account_number = account_number
        self.transaction_history = []

    def deposit(self, amount):
        if amount < 0:
            return "Invalid deposit amount"
        else:
            self.balance += amount
            self.transaction_history.append(f"Deposited {amount}. New balance: {self.balance}")
            print(f"Deposited {amount}. New balance is: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds, your balance is: {self.balance}")
        elif amount <= 0:
            print("Amount must be greater than 0")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount}. New balance: {self.balance}")
            print(f"Withdrew {amount}. New balance is: {self.balance}")

    def check_balance(self):
        print(f"Your current balance is: {self.balance}")

    def view_transaction_history(self):
        if self.transaction_history:
            print("Transaction history:")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions yet!")

def save_accounts(filename, accounts):
    with open(filename, 'w') as file:
        json.dump(accounts, file)

def load_accounts(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def main():
    filename = 'accounts.json'
    accounts = load_accounts(filename)

    account = None
    while True:
        print("\n--- Bank account menu ---")
        print("1. Create account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check balance")
        print("5. View transaction history")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_holder_name = input("Enter your name: ")

            if account_holder_name in accounts:
                print(f"Welcome back, {account_holder_name}!")
                account_data = accounts[account_holder_name]
                account = BankAccount(account_holder_name, account_data['balance'], account_data['account_number'])
                account.transaction_history = account_data['transaction_history']
                print("Account loaded successfully!")
            else:
                balance = float(input("Enter your initial balance: "))
                account_number = str(random.randint(1000000000, 9999999999))
                account = BankAccount(account_holder_name, balance, account_number)
                accounts[account_holder_name] = {
                    "balance": balance,
                    "account_number": account_number,
                    "transaction_history": account.transaction_history
                }
                print(f"Your account number is: {account_number}")
                print("Account created successfully")
                save_accounts(filename, accounts)

        elif choice == "2":
            if account:
                amount = float(input("Enter the deposit amount: "))
                account.deposit(amount)
                save_accounts(filename, accounts)  # Save the accounts after deposit
            else:
                print("You must create an account first!")
        
        elif choice == "3":
            if account:
                amount = float(input("Enter the withdrawal amount: "))
                account.withdraw(amount)
                save_accounts(filename, accounts)  # Save the accounts after withdrawal
            else:
                print("You must create an account first!")
        
        elif choice == "4":
            if account:
                account.check_balance()
            else:
                print("You must create an account first!")

        elif choice == "5":
            if account:
                account.view_transaction_history()
            else:
                print("You must create an account first!")

        elif choice == "6":
            print("Exiting program!")
            break

        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()