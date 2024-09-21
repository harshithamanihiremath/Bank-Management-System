# bank.py

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance):
        if account_number in self.accounts:
            return "Account already exists."
        self.accounts[account_number] = initial_balance
        return "Account created successfully."

    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            return "Account does not exist."
        if amount <= 0:
            return "Deposit amount must be positive."
        self.accounts[account_number] += amount
        return f"Successfully deposited {amount}. New balance: {self.accounts[account_number]}"

    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            return "Account does not exist."
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > self.accounts[account_number]:
            return "Insufficient funds."
        self.accounts[account_number] -= amount
        return f"Successfully withdrew {amount}. New balance: {self.accounts[account_number]}"

    def check_balance(self, account_number):
        if account_number not in self.accounts:
            return "Account does not exist."
        return f"Current balance: {self.accounts[account_number]}"
