class BankAccount:
    def __init__(self):
        self.__balance = 0

    def withdraw(self, amount):
        if amount > self.__balance :
            print(f"Error, Your balance ({self.__balance}) is less than the amount you entered")
        else:
            self.__balance -= amount
            print(f"You've withdrawn {amount}, your new balance is {self.__balance}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Your new balance is {self.__balance}")
        else:
            print("Invalid deposit")

    def checkbalance(self):
        print(f"Your balance is {self.__balance}")

account = BankAccount()
account.deposit(100)
account.withdraw(20)
account.withdraw(900)
account.checkbalance()
    