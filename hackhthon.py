import datetime

class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.add_transaction(f"Deposited: ${amount}")
            print(f"Successfully deposited ${amount}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.add_transaction(f"Withdrew: ${amount}")
            print(f"Successfully withdrew ${amount}.")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")
        return self.balance

    def add_transaction(self, description):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append(f"{timestamp} - {description}")

    def print_statement(self):
        print(f"Transaction statement for Account: {self.account_number}")
        for transaction in self.transactions:
            print(transaction)


class Bank:
    def __init__(self):
        self.accounts = {}
        self.account_counter = 1000

    def open_account(self, account_holder):
        self.account_counter += 1
        new_account = BankAccount(self.account_counter, account_holder)
        self.accounts[self.account_counter] = new_account
        print(f"Account successfully created! Account Number: {self.account_counter}")

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def transfer(self, sender_account_number, receiver_account_number, amount):
        sender = self.get_account(sender_account_number)
        receiver = self.get_account(receiver_account_number)

        if sender and receiver:
            if sender.balance >= amount:
                sender.withdraw(amount)
                receiver.deposit(amount)
                print(f"Successfully transferred ${amount} from {sender_account_number} to {receiver_account_number}.")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("Invalid account numbers.")

    def admin_check_total_deposit(self):
        total_deposits = sum(account.balance for account in self.accounts.values())
        print(f"Total deposits in the bank: ${total_deposits}")
        return total_deposits

    def admin_check_total_accounts(self):
        total_accounts = len(self.accounts)
        print(f"Total number of accounts in the bank: {total_accounts}")
        return total_accounts


def main():
    bank = Bank()

    while True:
        print("\nWelcome to the Banking System")
        print("1. Open Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transfer Money")
        print("6. Print Transaction Statement")
        print("7. Admin: Check Total Deposits")
        print("8. Admin: Check Total Accounts")
        print("9. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            account_holder = input("Enter account holder's name: ")
            bank.open_account(account_holder)

        elif choice == 2:
            account_number = int(input("Enter account number: "))
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            else:
                print("Invalid account number.")

        elif choice == 3:
            account_number = int(input("Enter account number: "))
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            else:
                print("Invalid account number.")

        elif choice == 4:
            account_number = int(input("Enter account number: "))
            account = bank.get_account(account_number)
            if account:
                account.check_balance()
            else:
                print("Invalid account number.")

        elif choice == 5:
            sender_account = int(input("Enter sender's account number: "))
            receiver_account = int(input("Enter receiver's account number: "))
            amount = float(input("Enter amount to transfer: "))
            bank.transfer(sender_account, receiver_account, amount)

        elif choice == 6:
            account_number = int(input("Enter account number: "))
            account = bank.get_account(account_number)
            if account:
                account.print_statement()
            else:
                print("Invalid account number.")

        elif choice == 7:
            bank.admin_check_total_deposit()

        elif choice == 8:
            bank.admin_check_total_accounts()

        elif choice == 9:
            print("Thank you for using the Banking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
