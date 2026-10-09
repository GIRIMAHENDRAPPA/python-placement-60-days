# Bank Account System - Week 3 OOPs Project

class BankAccount:
    def __init__(self, account_no, holder_name, balance=0):
        self.account_no = account_no
        self.holder_name = holder_name
        self.__balance = balance  # private - Encapsulation
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transactions.append(f"Deposited: {amount}")
            print(f"₹{amount} Deposited. New Balance: ₹{self.__balance}")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount <= self.__balance and amount > 0:
            self.__balance -= amount
            self.transactions.append(f"Withdrew: {amount}")
            print(f"₹{amount} Withdrawn. New Balance: ₹{self.__balance}")
        else:
            print("Insufficient balance or invalid amount!")

    def get_balance(self):
        return self.__balance

    def show_transactions(self):
        print(f"\n--- Transactions for {self.holder_name} ---")
        for t in self.transactions:
            print(t)

# Inheritance Example
class SavingsAccount(BankAccount):
    def __init__(self, account_no, holder_name, balance=0, interest_rate=4):
        super().__init__(account_no, holder_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        print(f"Interest Added: ₹{interest}")

# Main Bank System
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_no, name, balance=0):
        if account_no not in self.accounts:
            self.accounts[account_no] = SavingsAccount(account_no, name, balance)
            print(f"Account created for {name}")
        else:
            print("Account already exists!")

    def get_account(self, account_no):
        return self.accounts.get(account_no)

# --- Testing ---
bank = Bank()
bank.create_account("1001", "Anmol", 5000)

acc = bank.get_account("1001")
acc.deposit(2000)
acc.withdraw(1000)
print(f"Final Balance: ₹{acc.get_balance()}")
acc.add_interest()
acc.show_transactions()