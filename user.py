# user.py

from bank import Bank

def main():
    bank = Bank()
    
    while True:
        print("\nWelcome to the Bank Management System")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            account_number = input("Enter account number: ")
            initial_balance = float(input("Enter initial balance: "))
            print(bank.create_account(account_number, initial_balance))
        
        elif choice == '2':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            print(bank.deposit(account_number, amount))
        
        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            print(bank.withdraw(account_number, amount))
        
        elif choice == '4':
            account_number = input("Enter account number: ")
            print(bank.check_balance(account_number))
        
        elif choice == '5':
            print("Thank you for using the Bank Management System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
